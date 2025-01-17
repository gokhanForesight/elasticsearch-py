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
from .utils import _deprecated_options, query_params


class XPackClient(NamespacedClient):
    def __getattr__(self, attr_name):
        return getattr(self.client, attr_name)

    # AUTO-GENERATED-API-DEFINITIONS #
    @query_params("accept_enterprise", "categories")
    async def info(self, params=None, headers=None):
        """
        Retrieves information about the installed X-Pack features.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/master/info-api.html>`_

        :arg accept_enterprise: If this param is used it must be set to
            true
        :arg categories: Comma-separated list of info categories. Can be
            any of: build, license, features
        """
        client, params = _deprecated_options(self, params)
        return await client._perform_request(
            "GET", "/_xpack", params=params, headers=headers
        )

    @query_params("master_timeout")
    async def usage(self, params=None, headers=None):
        """
        Retrieves usage information about the installed X-Pack features.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/master/usage-api.html>`_

        :arg master_timeout: Specify timeout for watch write operation
        """
        client, params = _deprecated_options(self, params)
        return await client._perform_request(
            "GET", "/_xpack/usage", params=params, headers=headers
        )
