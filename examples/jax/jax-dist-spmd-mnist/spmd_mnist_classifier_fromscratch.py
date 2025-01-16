# Copyright 2024 kubeflow.org.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""An MNIST example with single-program multiple-data (SPMD) data parallelism.

The aim here is to illustrate how to use JAX's `pmap` to express and execute
SPMD programs for data parallelism along a batch dimension, while also
minimizing dependencies by avoiding the use of higher-level layers and
optimizers libraries.
"""

import multiprocessing
import os
import time
from functools import partial

import numpy as np
import numpy.random as npr

# JAX will treat your CPU as a single device by default, regardless of the number
# of cores available. Unfortunately, this means that using `pmap` is not possible out
# of the box – we’ll first need to instruct JAX to split the CPU into multiple devices.
# This variable has to be set before JAX or any library that imports it is imported

os.environ["XLA_FLAGS"] = "--xla_force_host_platform_device_count={}".format(
    multiprocessing.cpu_count()
)

import datasets  # noqa
import jax  # noqa
import jax.numpy as jnp  # noqa
from jax import grad, jit, lax, pmap  # noqa
from jax.scipy.special import logsumexp  # noqa
from jax.tree_util import tree_map  # noqa

jax.config.update("jax_cpu_collectives_implementation", "gloo")

process_id = int(os.getenv("PROCESS_ID"))
num_processes = int(os.getenv("NUM_PROCESSES"))
coordinator_address = (
    f"{os.getenv('COORDINATOR_ADDRESS')}:{int(os.getenv('COORDINATOR_PORT'))}"
)

jax.distributed.initialize(
    coordinator_address=coordinator_address,
    num_processes=num_processes,
    process_id=process_id,
)


def init_random_params(scale, layer_sizes, rng=npr.RandomState(0)):
    return [
        (scale * rng.randn(m, n), scale * rng.randn(n))
        for m, n, in zip(layer_sizes[:-1], layer_sizes[1:])
    ]


def predict(params, inputs):
    activations = inputs
    for w, b in params[:-1]:
        outputs = jnp.dot(activations, w) + b
        activations = jnp.tanh(outputs)

    final_w, final_b = params[-1]
    logits = jnp.dot(activations, final_w) + final_b
    return logits - logsumexp(logits, axis=1, keepdims=True)


def loss(params, batch):
    inputs, targets = batch
    preds = predict(params, inputs)
    return -jnp.mean(jnp.sum(preds * targets, axis=1))


@jit
def accuracy(params, batch):
    inputs, targets = batch
    target_class = jnp.argmax(targets, axis=1)
    predicted_class = jnp.argmax(predict(params, inputs), axis=1)
    return jnp.mean(predicted_class == target_class)


if __name__ == "__main__":
    layer_sizes = [784, 1024, 1024, 10]
    param_scale = 0.1
    step_size = 0.001
    num_epochs = 10
    # For this manual SPMD example, we get the number of devices (e.g. CPU,
    # GPUs or TPU cores) that we're using, and use it to reshape data minibatches.
    num_devices = jax.local_device_count()
    batch_size = num_devices * 5

    train_images, train_labels, test_images, test_labels = datasets.mnist()
    num_train = train_images.shape[0]
    num_complete_batches, leftover = divmod(num_train, batch_size)

    # Increasing number of batches requires more resources.
    num_batches = 10

    def data_stream():
        rng = npr.RandomState(0)
        while True:
            perm = rng.permutation(num_train)
            for i in range(num_batches):
                batch_idx = perm[i * batch_size : (i + 1) * batch_size]  # noqa
                images, labels = train_images[batch_idx], train_labels[batch_idx]
                # For this SPMD example, we reshape the data batch dimension into two
                # batch dimensions, one of which is mapped over parallel devices.
                batch_size_per_device, ragged = divmod(images.shape[0], num_devices)
                if ragged:
                    msg = "batch size must be divisible by device count, got {} and {}."
                    raise ValueError(msg.format(batch_size, num_devices))
                shape_prefix = (num_devices, batch_size_per_device)
                images = images.reshape(shape_prefix + images.shape[1:])
                labels = labels.reshape(shape_prefix + labels.shape[1:])
                yield images, labels

    batches = data_stream()

    @partial(pmap, axis_name="batch")
    def spmd_update(params, batch):
        grads = grad(loss)(params, batch)
        # We compute the total gradients, summing across the device-mapped axis,
        # using the `lax.psum` SPMD primitive, which does a fast all-reduce-sum.
        grads = [(lax.psum(dw, "batch"), lax.psum(db, "batch")) for dw, db in grads]
        return [
            (w - step_size * dw, b - step_size * db)
            for (w, b), (dw, db) in zip(params, grads)
        ]

    # We replicate the parameters so that the constituent arrays have a leading
    # dimension of size equal to the number of devices we're pmapping over.
    init_params = init_random_params(param_scale, layer_sizes)

    def replicate_array(x):
        return np.broadcast_to(x, (num_devices,) + x.shape)

    replicated_params = tree_map(replicate_array, init_params)

    print(f"JAX global devices:{jax.devices()}")
    print(f"JAX local devices:{jax.local_devices()}")

    print(f"JAX device count:{jax.device_count()}")
    print(f"JAX local device count:{jax.local_device_count()}")
    print(f"JAX process count:{jax.process_count()}")

    for epoch in range(num_epochs):
        start_time = time.time()
        for _ in range(num_batches):
            replicated_params = spmd_update(replicated_params, next(batches))
        epoch_time = time.time() - start_time

        # We evaluate using the jitted `accuracy` function (not using pmap) by
        # grabbing just one of the replicated parameter values.
        params = tree_map(lambda x: x[0], replicated_params)
        train_acc = accuracy(params, (train_images, train_labels))
        test_acc = accuracy(params, (test_images, test_labels))
        print(f"Epoch {epoch} in {epoch_time:0.2f} sec")
        print(f"Training set accuracy {train_acc}")
        print(f"Test set accuracy {test_acc}")
