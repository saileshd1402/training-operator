# Copyright 2016 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

FROM tensorflow/tensorflow:2.17.0

# Using keras-2.17 because of bug on keras-3.4.1
# which used by default by TF-2.17 (https://github.com/tensorflow/tensorflow/issues/72388)
ENV TF_USE_LEGACY_KERAS 1
RUN pip install tf_keras

ADD examples/tensorflow/dist-mnist/ /var/tf_dist_mnist
ADD examples/tensorflow/mnist_utils.py /var/tf_dist_mnist
ENTRYPOINT ["python", "/var/tf_dist_mnist/dist_mnist.py"]
