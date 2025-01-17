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


class GraphClient(NamespacedClient):
    @query_params("routing", "timeout")
    async def explore(self, index, body=None, params=None, headers=None):
        """
        Explore extracted and summarized information about the documents and terms in
        an index.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/master/graph-explore-api.html>`_

        :arg index: A comma-separated list of index names to search; use
            `_all` or empty string to perform the operation on all indices
        :arg body: Graph Query DSL
        :arg routing: Specific routing value
        :arg timeout: Explicit operation timeout
        """
        client, params = _deprecated_options(self, params)
        if index in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'index'.")

        return await client._perform_request(
            "POST",
            _make_path(index, "_graph", "explore"),
            params=params,
            headers=headers,
            body=body,
        )
