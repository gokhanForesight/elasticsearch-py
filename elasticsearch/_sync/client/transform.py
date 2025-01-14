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


class TransformClient(NamespacedClient):
    @query_params("force")
    def delete_transform(self, transform_id, params=None, headers=None):
        """
        Deletes an existing transform.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/master/delete-transform.html>`_

        :arg transform_id: The id of the transform to delete
        :arg force: When `true`, the transform is deleted regardless of
            its current state. The default value is `false`, meaning that the
            transform must be `stopped` before it can be deleted.
        """
        client, params = _deprecated_options(self, params)
        if transform_id in SKIP_IN_PATH:
            raise ValueError(
                "Empty value passed for a required argument 'transform_id'."
            )

        return client._perform_request(
            "DELETE",
            _make_path("_transform", transform_id),
            params=params,
            headers=headers,
        )

    @query_params("allow_no_match", "exclude_generated", "from_", "size")
    def get_transform(self, transform_id=None, params=None, headers=None):
        """
        Retrieves configuration information for transforms.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/master/get-transform.html>`_

        :arg transform_id: The id or comma delimited list of id
            expressions of the transforms to get, '_all' or '*' implies get all
            transforms
        :arg allow_no_match: Whether to ignore if a wildcard expression
            matches no transforms. (This includes `_all` string or when no
            transforms have been specified)
        :arg exclude_generated: Omits fields that are illegal to set on
            transform PUT
        :arg from\\_: skips a number of transform configs, defaults to 0
        :arg size: specifies a max number of transforms to get, defaults
            to 100
        """
        client, params = _deprecated_options(self, params)
        if params and "from_" in params:
            params["from"] = params.pop("from_")

        return client._perform_request(
            "GET",
            _make_path("_transform", transform_id),
            params=params,
            headers=headers,
        )

    @query_params("allow_no_match", "from_", "size")
    def get_transform_stats(self, transform_id, params=None, headers=None):
        """
        Retrieves usage information for transforms.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/master/get-transform-stats.html>`_

        :arg transform_id: The id of the transform for which to get
            stats. '_all' or '*' implies all transforms
        :arg allow_no_match: Whether to ignore if a wildcard expression
            matches no transforms. (This includes `_all` string or when no
            transforms have been specified)
        :arg from\\_: skips a number of transform stats, defaults to 0
        :arg size: specifies a max number of transform stats to get,
            defaults to 100
        """
        client, params = _deprecated_options(self, params)
        if params and "from_" in params:
            params["from"] = params.pop("from_")

        if transform_id in SKIP_IN_PATH:
            raise ValueError(
                "Empty value passed for a required argument 'transform_id'."
            )

        return client._perform_request(
            "GET",
            _make_path("_transform", transform_id, "_stats"),
            params=params,
            headers=headers,
        )

    @query_params()
    def preview_transform(
        self, body=None, transform_id=None, params=None, headers=None
    ):
        """
        Previews a transform.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/master/preview-transform.html>`_

        :arg body: The definition for the transform to preview
        :arg transform_id: The id of the transform to preview.
        """
        client, params = _deprecated_options(self, params)
        return client._perform_request(
            "POST",
            _make_path("_transform", transform_id, "_preview"),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params("defer_validation")
    def put_transform(self, transform_id, body, params=None, headers=None):
        """
        Instantiates a transform.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/master/put-transform.html>`_

        :arg transform_id: The id of the new transform.
        :arg body: The transform definition
        :arg defer_validation: If validations should be deferred until
            transform starts, defaults to false.
        """
        client, params = _deprecated_options(self, params)
        for param in (transform_id, body):
            if param in SKIP_IN_PATH:
                raise ValueError("Empty value passed for a required argument.")

        return client._perform_request(
            "PUT",
            _make_path("_transform", transform_id),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params("timeout")
    def start_transform(self, transform_id, params=None, headers=None):
        """
        Starts one or more transforms.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/master/start-transform.html>`_

        :arg transform_id: The id of the transform to start
        :arg timeout: Controls the time to wait for the transform to
            start
        """
        client, params = _deprecated_options(self, params)
        if transform_id in SKIP_IN_PATH:
            raise ValueError(
                "Empty value passed for a required argument 'transform_id'."
            )

        return client._perform_request(
            "POST",
            _make_path("_transform", transform_id, "_start"),
            params=params,
            headers=headers,
        )

    @query_params(
        "allow_no_match",
        "force",
        "timeout",
        "wait_for_checkpoint",
        "wait_for_completion",
    )
    def stop_transform(self, transform_id, params=None, headers=None):
        """
        Stops one or more transforms.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/master/stop-transform.html>`_

        :arg transform_id: The id of the transform to stop
        :arg allow_no_match: Whether to ignore if a wildcard expression
            matches no transforms. (This includes `_all` string or when no
            transforms have been specified)
        :arg force: Whether to force stop a failed transform or not.
            Default to false
        :arg timeout: Controls the time to wait until the transform has
            stopped. Default to 30 seconds
        :arg wait_for_checkpoint: Whether to wait for the transform to
            reach a checkpoint before stopping. Default to false
        :arg wait_for_completion: Whether to wait for the transform to
            fully stop before returning or not. Default to false
        """
        client, params = _deprecated_options(self, params)
        if transform_id in SKIP_IN_PATH:
            raise ValueError(
                "Empty value passed for a required argument 'transform_id'."
            )

        return client._perform_request(
            "POST",
            _make_path("_transform", transform_id, "_stop"),
            params=params,
            headers=headers,
        )

    @query_params("defer_validation")
    def update_transform(self, transform_id, body, params=None, headers=None):
        """
        Updates certain properties of a transform.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/master/update-transform.html>`_

        :arg transform_id: The id of the transform.
        :arg body: The update transform definition
        :arg defer_validation: If validations should be deferred until
            transform starts, defaults to false.
        """
        client, params = _deprecated_options(self, params)
        for param in (transform_id, body):
            if param in SKIP_IN_PATH:
                raise ValueError("Empty value passed for a required argument.")

        return client._perform_request(
            "POST",
            _make_path("_transform", transform_id, "_update"),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params("dry_run")
    def upgrade_transforms(self, params=None, headers=None):
        """
        Upgrades all transforms.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/master/upgrade-transforms.html>`_

        :arg dry_run: Whether to only check for updates but don't
            execute
        """
        client, params = _deprecated_options(self, params)
        return client._perform_request(
            "POST", "/_transform/_upgrade", params=params, headers=headers
        )
