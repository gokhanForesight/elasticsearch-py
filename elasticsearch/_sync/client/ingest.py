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


class IngestClient(NamespacedClient):
    @query_params("master_timeout", "summary")
    def get_pipeline(self, id=None, params=None, headers=None):
        """
        Returns a pipeline.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/master/get-pipeline-api.html>`_

        :arg id: Comma separated list of pipeline ids. Wildcards
            supported
        :arg master_timeout: Explicit operation timeout for connection
            to master node
        :arg summary: Return pipelines without their definitions
            (default: false)
        """
        client, params = _deprecated_options(self, params)
        return client._perform_request(
            "GET", _make_path("_ingest", "pipeline", id), params=params, headers=headers
        )

    @query_params("if_version", "master_timeout", "timeout")
    def put_pipeline(self, id, body, params=None, headers=None):
        """
        Creates or updates a pipeline.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/master/put-pipeline-api.html>`_

        :arg id: Pipeline ID
        :arg body: The ingest definition
        :arg if_version: Required version for optimistic concurrency
            control for pipeline updates
        :arg master_timeout: Explicit operation timeout for connection
            to master node
        :arg timeout: Explicit operation timeout
        """
        client, params = _deprecated_options(self, params)
        for param in (id, body):
            if param in SKIP_IN_PATH:
                raise ValueError("Empty value passed for a required argument.")

        return client._perform_request(
            "PUT",
            _make_path("_ingest", "pipeline", id),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params("master_timeout", "timeout")
    def delete_pipeline(self, id, params=None, headers=None):
        """
        Deletes a pipeline.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/master/delete-pipeline-api.html>`_

        :arg id: Pipeline ID
        :arg master_timeout: Explicit operation timeout for connection
            to master node
        :arg timeout: Explicit operation timeout
        """
        client, params = _deprecated_options(self, params)
        if id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'id'.")

        return client._perform_request(
            "DELETE",
            _make_path("_ingest", "pipeline", id),
            params=params,
            headers=headers,
        )

    @query_params("verbose")
    def simulate(self, body, id=None, params=None, headers=None):
        """
        Allows to simulate a pipeline with example documents.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/master/simulate-pipeline-api.html>`_

        :arg body: The simulate definition
        :arg id: Pipeline ID
        :arg verbose: Verbose mode. Display data output for each
            processor in executed pipeline
        """
        client, params = _deprecated_options(self, params)
        if body in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'body'.")

        return client._perform_request(
            "POST",
            _make_path("_ingest", "pipeline", id, "_simulate"),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params()
    def processor_grok(self, params=None, headers=None):
        """
        Returns a list of the built-in patterns.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/master/grok-processor.html#grok-processor-rest-get>`_
        """
        client, params = _deprecated_options(self, params)
        return client._perform_request(
            "GET", "/_ingest/processor/grok", params=params, headers=headers
        )

    @query_params()
    def geo_ip_stats(self, params=None, headers=None):
        """
        Returns statistical information about geoip databases

        `<https://www.elastic.co/guide/en/elasticsearch/reference/master/geoip-stats-api.html>`_
        """
        client, params = _deprecated_options(self, params)
        return client._perform_request(
            "GET", "/_ingest/geoip/stats", params=params, headers=headers
        )
