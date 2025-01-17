#  Licensed to Elasticsearch B.V. under one or more contributor
#  license agreements. See the NOTICE file distributed with
#  this work for additional information regarding copyright
#  ownership. Elasticsearch B.V. licenses this file to you under
#  the Apache License, Version 2.0 (the "License"); you may
#  not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
# 	http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing,
#  software distributed under the License is distributed on an
#  "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
#  KIND, either express or implied.  See the License for the
#  specific language governing permissions and limitations
#  under the License.

from ._base import NamespacedClient
from .utils import SKIP_IN_PATH, _deprecated_options, _make_path, query_params


class CcrClient(NamespacedClient):
    @query_params()
    def delete_auto_follow_pattern(self, name, params=None, headers=None):
        """
        Deletes auto-follow patterns.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/master/ccr-delete-auto-follow-pattern.html>`_

        :arg name: The name of the auto follow pattern.
        """
        client, params = _deprecated_options(self, params)
        if name in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'name'.")

        return client._perform_request(
            "DELETE",
            _make_path("_ccr", "auto_follow", name),
            params=params,
            headers=headers,
        )

    @query_params("wait_for_active_shards")
    def follow(self, index, body, params=None, headers=None):
        """
        Creates a new follower index configured to follow the referenced leader index.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/master/ccr-put-follow.html>`_

        :arg index: The name of the follower index
        :arg body: The name of the leader index and other optional ccr
            related parameters
        :arg wait_for_active_shards: Sets the number of shard copies
            that must be active before returning. Defaults to 0. Set to `all` for
            all shard copies, otherwise set to any non-negative value less than or
            equal to the total number of copies for the shard (number of replicas +
            1)  Default: 0
        """
        client, params = _deprecated_options(self, params)
        for param in (index, body):
            if param in SKIP_IN_PATH:
                raise ValueError("Empty value passed for a required argument.")

        return client._perform_request(
            "PUT",
            _make_path(index, "_ccr", "follow"),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params()
    def follow_info(self, index, params=None, headers=None):
        """
        Retrieves information about all follower indices, including parameters and
        status for each follower index

        `<https://www.elastic.co/guide/en/elasticsearch/reference/master/ccr-get-follow-info.html>`_

        :arg index: A comma-separated list of index patterns; use `_all`
            to perform the operation on all indices
        """
        client, params = _deprecated_options(self, params)
        if index in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'index'.")

        return client._perform_request(
            "GET", _make_path(index, "_ccr", "info"), params=params, headers=headers
        )

    @query_params()
    def follow_stats(self, index, params=None, headers=None):
        """
        Retrieves follower stats. return shard-level stats about the following tasks
        associated with each shard for the specified indices.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/master/ccr-get-follow-stats.html>`_

        :arg index: A comma-separated list of index patterns; use `_all`
            to perform the operation on all indices
        """
        client, params = _deprecated_options(self, params)
        if index in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'index'.")

        return client._perform_request(
            "GET", _make_path(index, "_ccr", "stats"), params=params, headers=headers
        )

    @query_params()
    def forget_follower(self, index, body, params=None, headers=None):
        """
        Removes the follower retention leases from the leader.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/master/ccr-post-forget-follower.html>`_

        :arg index: the name of the leader index for which specified
            follower retention leases should be removed
        :arg body: the name and UUID of the follower index, the name of
            the cluster containing the follower index, and the alias from the
            perspective of that cluster for the remote cluster containing the leader
            index
        """
        client, params = _deprecated_options(self, params)
        for param in (index, body):
            if param in SKIP_IN_PATH:
                raise ValueError("Empty value passed for a required argument.")

        return client._perform_request(
            "POST",
            _make_path(index, "_ccr", "forget_follower"),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params()
    def get_auto_follow_pattern(self, name=None, params=None, headers=None):
        """
        Gets configured auto-follow patterns. Returns the specified auto-follow pattern
        collection.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/master/ccr-get-auto-follow-pattern.html>`_

        :arg name: The name of the auto follow pattern.
        """
        client, params = _deprecated_options(self, params)
        return client._perform_request(
            "GET",
            _make_path("_ccr", "auto_follow", name),
            params=params,
            headers=headers,
        )

    @query_params()
    def pause_follow(self, index, params=None, headers=None):
        """
        Pauses a follower index. The follower index will not fetch any additional
        operations from the leader index.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/master/ccr-post-pause-follow.html>`_

        :arg index: The name of the follower index that should pause
            following its leader index.
        """
        client, params = _deprecated_options(self, params)
        if index in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'index'.")

        return client._perform_request(
            "POST",
            _make_path(index, "_ccr", "pause_follow"),
            params=params,
            headers=headers,
        )

    @query_params()
    def put_auto_follow_pattern(self, name, body, params=None, headers=None):
        """
        Creates a new named collection of auto-follow patterns against a specified
        remote cluster. Newly created indices on the remote cluster matching any of the
        specified patterns will be automatically configured as follower indices.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/master/ccr-put-auto-follow-pattern.html>`_

        :arg name: The name of the auto follow pattern.
        :arg body: The specification of the auto follow pattern
        """
        client, params = _deprecated_options(self, params)
        for param in (name, body):
            if param in SKIP_IN_PATH:
                raise ValueError("Empty value passed for a required argument.")

        return client._perform_request(
            "PUT",
            _make_path("_ccr", "auto_follow", name),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params()
    def resume_follow(self, index, body=None, params=None, headers=None):
        """
        Resumes a follower index that has been paused

        `<https://www.elastic.co/guide/en/elasticsearch/reference/master/ccr-post-resume-follow.html>`_

        :arg index: The name of the follow index to resume following.
        :arg body: The name of the leader index and other optional ccr
            related parameters
        """
        client, params = _deprecated_options(self, params)
        if index in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'index'.")

        return client._perform_request(
            "POST",
            _make_path(index, "_ccr", "resume_follow"),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params()
    def stats(self, params=None, headers=None):
        """
        Gets all stats related to cross-cluster replication.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/master/ccr-get-stats.html>`_
        """
        client, params = _deprecated_options(self, params)
        return client._perform_request(
            "GET", "/_ccr/stats", params=params, headers=headers
        )

    @query_params()
    def unfollow(self, index, params=None, headers=None):
        """
        Stops the following task associated with a follower index and removes index
        metadata and settings associated with cross-cluster replication.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/master/ccr-post-unfollow.html>`_

        :arg index: The name of the follower index that should be turned
            into a regular index.
        """
        client, params = _deprecated_options(self, params)
        if index in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'index'.")

        return client._perform_request(
            "POST",
            _make_path(index, "_ccr", "unfollow"),
            params=params,
            headers=headers,
        )

    @query_params()
    def pause_auto_follow_pattern(self, name, params=None, headers=None):
        """
        Pauses an auto-follow pattern

        `<https://www.elastic.co/guide/en/elasticsearch/reference/master/ccr-pause-auto-follow-pattern.html>`_

        :arg name: The name of the auto follow pattern that should pause
            discovering new indices to follow.
        """
        client, params = _deprecated_options(self, params)
        if name in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'name'.")

        return client._perform_request(
            "POST",
            _make_path("_ccr", "auto_follow", name, "pause"),
            params=params,
            headers=headers,
        )

    @query_params()
    def resume_auto_follow_pattern(self, name, params=None, headers=None):
        """
        Resumes an auto-follow pattern that has been paused

        `<https://www.elastic.co/guide/en/elasticsearch/reference/master/ccr-resume-auto-follow-pattern.html>`_

        :arg name: The name of the auto follow pattern to resume
            discovering new indices to follow.
        """
        client, params = _deprecated_options(self, params)
        if name in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'name'.")

        return client._perform_request(
            "POST",
            _make_path("_ccr", "auto_follow", name, "resume"),
            params=params,
            headers=headers,
        )
