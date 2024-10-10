// Copyright 2024 The Kubeflow Authors
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

// Code generated by lister-gen. DO NOT EDIT.

package v1

import (
	v1 "github.com/kubeflow/training-operator/pkg/apis/kubeflow.org/v1"
	"k8s.io/apimachinery/pkg/api/errors"
	"k8s.io/apimachinery/pkg/labels"
	"k8s.io/client-go/tools/cache"
)

// PaddleJobLister helps list PaddleJobs.
// All objects returned here must be treated as read-only.
type PaddleJobLister interface {
	// List lists all PaddleJobs in the indexer.
	// Objects returned here must be treated as read-only.
	List(selector labels.Selector) (ret []*v1.PaddleJob, err error)
	// PaddleJobs returns an object that can list and get PaddleJobs.
	PaddleJobs(namespace string) PaddleJobNamespaceLister
	PaddleJobListerExpansion
}

// paddleJobLister implements the PaddleJobLister interface.
type paddleJobLister struct {
	indexer cache.Indexer
}

// NewPaddleJobLister returns a new PaddleJobLister.
func NewPaddleJobLister(indexer cache.Indexer) PaddleJobLister {
	return &paddleJobLister{indexer: indexer}
}

// List lists all PaddleJobs in the indexer.
func (s *paddleJobLister) List(selector labels.Selector) (ret []*v1.PaddleJob, err error) {
	err = cache.ListAll(s.indexer, selector, func(m interface{}) {
		ret = append(ret, m.(*v1.PaddleJob))
	})
	return ret, err
}

// PaddleJobs returns an object that can list and get PaddleJobs.
func (s *paddleJobLister) PaddleJobs(namespace string) PaddleJobNamespaceLister {
	return paddleJobNamespaceLister{indexer: s.indexer, namespace: namespace}
}

// PaddleJobNamespaceLister helps list and get PaddleJobs.
// All objects returned here must be treated as read-only.
type PaddleJobNamespaceLister interface {
	// List lists all PaddleJobs in the indexer for a given namespace.
	// Objects returned here must be treated as read-only.
	List(selector labels.Selector) (ret []*v1.PaddleJob, err error)
	// Get retrieves the PaddleJob from the indexer for a given namespace and name.
	// Objects returned here must be treated as read-only.
	Get(name string) (*v1.PaddleJob, error)
	PaddleJobNamespaceListerExpansion
}

// paddleJobNamespaceLister implements the PaddleJobNamespaceLister
// interface.
type paddleJobNamespaceLister struct {
	indexer   cache.Indexer
	namespace string
}

// List lists all PaddleJobs in the indexer for a given namespace.
func (s paddleJobNamespaceLister) List(selector labels.Selector) (ret []*v1.PaddleJob, err error) {
	err = cache.ListAllByNamespace(s.indexer, s.namespace, selector, func(m interface{}) {
		ret = append(ret, m.(*v1.PaddleJob))
	})
	return ret, err
}

// Get retrieves the PaddleJob from the indexer for a given namespace and name.
func (s paddleJobNamespaceLister) Get(name string) (*v1.PaddleJob, error) {
	obj, exists, err := s.indexer.GetByKey(s.namespace + "/" + name)
	if err != nil {
		return nil, err
	}
	if !exists {
		return nil, errors.NewNotFound(v1.Resource("paddlejob"), name)
	}
	return obj.(*v1.PaddleJob), nil
}
