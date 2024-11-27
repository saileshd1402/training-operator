# coding: utf-8

"""
    Kubeflow Training SDK

    Python SDK for Kubeflow Training  # noqa: E501

    The version of the OpenAPI document: v1.7.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from kubeflow.training.configuration import Configuration


class V1ListOptions(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'allow_watch_bookmarks': 'bool',
        'api_version': 'str',
        '_continue': 'str',
        'field_selector': 'str',
        'kind': 'str',
        'label_selector': 'str',
        'limit': 'int',
        'resource_version': 'str',
        'resource_version_match': 'str',
        'send_initial_events': 'bool',
        'timeout_seconds': 'int',
        'watch': 'bool'
    }

    attribute_map = {
        'allow_watch_bookmarks': 'allowWatchBookmarks',
        'api_version': 'apiVersion',
        '_continue': 'continue',
        'field_selector': 'fieldSelector',
        'kind': 'kind',
        'label_selector': 'labelSelector',
        'limit': 'limit',
        'resource_version': 'resourceVersion',
        'resource_version_match': 'resourceVersionMatch',
        'send_initial_events': 'sendInitialEvents',
        'timeout_seconds': 'timeoutSeconds',
        'watch': 'watch'
    }

    def __init__(self, allow_watch_bookmarks=None, api_version=None, _continue=None, field_selector=None, kind=None, label_selector=None, limit=None, resource_version=None, resource_version_match=None, send_initial_events=None, timeout_seconds=None, watch=None, local_vars_configuration=None):  # noqa: E501
        """V1ListOptions - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._allow_watch_bookmarks = None
        self._api_version = None
        self.__continue = None
        self._field_selector = None
        self._kind = None
        self._label_selector = None
        self._limit = None
        self._resource_version = None
        self._resource_version_match = None
        self._send_initial_events = None
        self._timeout_seconds = None
        self._watch = None
        self.discriminator = None

        if allow_watch_bookmarks is not None:
            self.allow_watch_bookmarks = allow_watch_bookmarks
        if api_version is not None:
            self.api_version = api_version
        if _continue is not None:
            self._continue = _continue
        if field_selector is not None:
            self.field_selector = field_selector
        if kind is not None:
            self.kind = kind
        if label_selector is not None:
            self.label_selector = label_selector
        if limit is not None:
            self.limit = limit
        if resource_version is not None:
            self.resource_version = resource_version
        if resource_version_match is not None:
            self.resource_version_match = resource_version_match
        if send_initial_events is not None:
            self.send_initial_events = send_initial_events
        if timeout_seconds is not None:
            self.timeout_seconds = timeout_seconds
        if watch is not None:
            self.watch = watch

    @property
    def allow_watch_bookmarks(self):
        """Gets the allow_watch_bookmarks of this V1ListOptions.  # noqa: E501

        allowWatchBookmarks requests watch events with type \"BOOKMARK\". Servers that do not implement bookmarks may ignore this flag and bookmarks are sent at the server's discretion. Clients should not assume bookmarks are returned at any specific interval, nor may they assume the server will send any BOOKMARK event during a session. If this is not a watch, this field is ignored.  # noqa: E501

        :return: The allow_watch_bookmarks of this V1ListOptions.  # noqa: E501
        :rtype: bool
        """
        return self._allow_watch_bookmarks

    @allow_watch_bookmarks.setter
    def allow_watch_bookmarks(self, allow_watch_bookmarks):
        """Sets the allow_watch_bookmarks of this V1ListOptions.

        allowWatchBookmarks requests watch events with type \"BOOKMARK\". Servers that do not implement bookmarks may ignore this flag and bookmarks are sent at the server's discretion. Clients should not assume bookmarks are returned at any specific interval, nor may they assume the server will send any BOOKMARK event during a session. If this is not a watch, this field is ignored.  # noqa: E501

        :param allow_watch_bookmarks: The allow_watch_bookmarks of this V1ListOptions.  # noqa: E501
        :type: bool
        """

        self._allow_watch_bookmarks = allow_watch_bookmarks

    @property
    def api_version(self):
        """Gets the api_version of this V1ListOptions.  # noqa: E501

        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources  # noqa: E501

        :return: The api_version of this V1ListOptions.  # noqa: E501
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """Sets the api_version of this V1ListOptions.

        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources  # noqa: E501

        :param api_version: The api_version of this V1ListOptions.  # noqa: E501
        :type: str
        """

        self._api_version = api_version

    @property
    def _continue(self):
        """Gets the _continue of this V1ListOptions.  # noqa: E501

        The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \"next key\".  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications.  # noqa: E501

        :return: The _continue of this V1ListOptions.  # noqa: E501
        :rtype: str
        """
        return self.__continue

    @_continue.setter
    def _continue(self, _continue):
        """Sets the _continue of this V1ListOptions.

        The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \"next key\".  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications.  # noqa: E501

        :param _continue: The _continue of this V1ListOptions.  # noqa: E501
        :type: str
        """

        self.__continue = _continue

    @property
    def field_selector(self):
        """Gets the field_selector of this V1ListOptions.  # noqa: E501

        A selector to restrict the list of returned objects by their fields. Defaults to everything.  # noqa: E501

        :return: The field_selector of this V1ListOptions.  # noqa: E501
        :rtype: str
        """
        return self._field_selector

    @field_selector.setter
    def field_selector(self, field_selector):
        """Sets the field_selector of this V1ListOptions.

        A selector to restrict the list of returned objects by their fields. Defaults to everything.  # noqa: E501

        :param field_selector: The field_selector of this V1ListOptions.  # noqa: E501
        :type: str
        """

        self._field_selector = field_selector

    @property
    def kind(self):
        """Gets the kind of this V1ListOptions.  # noqa: E501

        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds  # noqa: E501

        :return: The kind of this V1ListOptions.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this V1ListOptions.

        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds  # noqa: E501

        :param kind: The kind of this V1ListOptions.  # noqa: E501
        :type: str
        """

        self._kind = kind

    @property
    def label_selector(self):
        """Gets the label_selector of this V1ListOptions.  # noqa: E501

        A selector to restrict the list of returned objects by their labels. Defaults to everything.  # noqa: E501

        :return: The label_selector of this V1ListOptions.  # noqa: E501
        :rtype: str
        """
        return self._label_selector

    @label_selector.setter
    def label_selector(self, label_selector):
        """Sets the label_selector of this V1ListOptions.

        A selector to restrict the list of returned objects by their labels. Defaults to everything.  # noqa: E501

        :param label_selector: The label_selector of this V1ListOptions.  # noqa: E501
        :type: str
        """

        self._label_selector = label_selector

    @property
    def limit(self):
        """Gets the limit of this V1ListOptions.  # noqa: E501

        limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned.  # noqa: E501

        :return: The limit of this V1ListOptions.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this V1ListOptions.

        limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned.  # noqa: E501

        :param limit: The limit of this V1ListOptions.  # noqa: E501
        :type: int
        """

        self._limit = limit

    @property
    def resource_version(self):
        """Gets the resource_version of this V1ListOptions.  # noqa: E501

        resourceVersion sets a constraint on what resource versions a request may be served from. See https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions for details.  Defaults to unset  # noqa: E501

        :return: The resource_version of this V1ListOptions.  # noqa: E501
        :rtype: str
        """
        return self._resource_version

    @resource_version.setter
    def resource_version(self, resource_version):
        """Sets the resource_version of this V1ListOptions.

        resourceVersion sets a constraint on what resource versions a request may be served from. See https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions for details.  Defaults to unset  # noqa: E501

        :param resource_version: The resource_version of this V1ListOptions.  # noqa: E501
        :type: str
        """

        self._resource_version = resource_version

    @property
    def resource_version_match(self):
        """Gets the resource_version_match of this V1ListOptions.  # noqa: E501

        resourceVersionMatch determines how resourceVersion is applied to list calls. It is highly recommended that resourceVersionMatch be set for list calls where resourceVersion is set See https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions for details.  Defaults to unset  # noqa: E501

        :return: The resource_version_match of this V1ListOptions.  # noqa: E501
        :rtype: str
        """
        return self._resource_version_match

    @resource_version_match.setter
    def resource_version_match(self, resource_version_match):
        """Sets the resource_version_match of this V1ListOptions.

        resourceVersionMatch determines how resourceVersion is applied to list calls. It is highly recommended that resourceVersionMatch be set for list calls where resourceVersion is set See https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions for details.  Defaults to unset  # noqa: E501

        :param resource_version_match: The resource_version_match of this V1ListOptions.  # noqa: E501
        :type: str
        """

        self._resource_version_match = resource_version_match

    @property
    def send_initial_events(self):
        """Gets the send_initial_events of this V1ListOptions.  # noqa: E501

        `sendInitialEvents=true` may be set together with `watch=true`. In that case, the watch stream will begin with synthetic events to produce the current state of objects in the collection. Once all such events have been sent, a synthetic \"Bookmark\" event  will be sent. The bookmark will report the ResourceVersion (RV) corresponding to the set of objects, and be marked with `\"k8s.io/initial-events-end\": \"true\"` annotation. Afterwards, the watch stream will proceed as usual, sending watch events corresponding to changes (subsequent to the RV) to objects watched.  When `sendInitialEvents` option is set, we require `resourceVersionMatch` option to also be set. The semantic of the watch request is as following: - `resourceVersionMatch` = NotOlderThan   is interpreted as \"data at least as new as the provided `resourceVersion`\"   and the bookmark event is send when the state is synced   to a `resourceVersion` at least as fresh as the one provided by the ListOptions.   If `resourceVersion` is unset, this is interpreted as \"consistent read\" and the   bookmark event is send when the state is synced at least to the moment   when request started being processed. - `resourceVersionMatch` set to any other value or unset   Invalid error is returned.  Defaults to true if `resourceVersion=\"\"` or `resourceVersion=\"0\"` (for backward compatibility reasons) and to false otherwise.  # noqa: E501

        :return: The send_initial_events of this V1ListOptions.  # noqa: E501
        :rtype: bool
        """
        return self._send_initial_events

    @send_initial_events.setter
    def send_initial_events(self, send_initial_events):
        """Sets the send_initial_events of this V1ListOptions.

        `sendInitialEvents=true` may be set together with `watch=true`. In that case, the watch stream will begin with synthetic events to produce the current state of objects in the collection. Once all such events have been sent, a synthetic \"Bookmark\" event  will be sent. The bookmark will report the ResourceVersion (RV) corresponding to the set of objects, and be marked with `\"k8s.io/initial-events-end\": \"true\"` annotation. Afterwards, the watch stream will proceed as usual, sending watch events corresponding to changes (subsequent to the RV) to objects watched.  When `sendInitialEvents` option is set, we require `resourceVersionMatch` option to also be set. The semantic of the watch request is as following: - `resourceVersionMatch` = NotOlderThan   is interpreted as \"data at least as new as the provided `resourceVersion`\"   and the bookmark event is send when the state is synced   to a `resourceVersion` at least as fresh as the one provided by the ListOptions.   If `resourceVersion` is unset, this is interpreted as \"consistent read\" and the   bookmark event is send when the state is synced at least to the moment   when request started being processed. - `resourceVersionMatch` set to any other value or unset   Invalid error is returned.  Defaults to true if `resourceVersion=\"\"` or `resourceVersion=\"0\"` (for backward compatibility reasons) and to false otherwise.  # noqa: E501

        :param send_initial_events: The send_initial_events of this V1ListOptions.  # noqa: E501
        :type: bool
        """

        self._send_initial_events = send_initial_events

    @property
    def timeout_seconds(self):
        """Gets the timeout_seconds of this V1ListOptions.  # noqa: E501

        Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity.  # noqa: E501

        :return: The timeout_seconds of this V1ListOptions.  # noqa: E501
        :rtype: int
        """
        return self._timeout_seconds

    @timeout_seconds.setter
    def timeout_seconds(self, timeout_seconds):
        """Sets the timeout_seconds of this V1ListOptions.

        Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity.  # noqa: E501

        :param timeout_seconds: The timeout_seconds of this V1ListOptions.  # noqa: E501
        :type: int
        """

        self._timeout_seconds = timeout_seconds

    @property
    def watch(self):
        """Gets the watch of this V1ListOptions.  # noqa: E501

        Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion.  # noqa: E501

        :return: The watch of this V1ListOptions.  # noqa: E501
        :rtype: bool
        """
        return self._watch

    @watch.setter
    def watch(self, watch):
        """Sets the watch of this V1ListOptions.

        Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion.  # noqa: E501

        :param watch: The watch of this V1ListOptions.  # noqa: E501
        :type: bool
        """

        self._watch = watch

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1ListOptions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1ListOptions):
            return True

        return self.to_dict() != other.to_dict()