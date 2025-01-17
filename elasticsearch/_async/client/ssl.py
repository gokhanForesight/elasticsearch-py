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


class SslClient(NamespacedClient):
    @query_params()
    async def certificates(self, params=None, headers=None):
        """
        Retrieves information about the X.509 certificates used to encrypt
        communications in the cluster.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/master/security-api-ssl.html>`_
        """
        client, params = _deprecated_options(self, params)
        return await client._perform_request(
            "GET", "/_ssl/certificates", params=params, headers=headers
        )
