# SPDX-License-Identifier: Apache-2.0
#
# The OpenSearch Contributors require contributions made to
# this file be licensed under the Apache-2.0 license or a
# compatible open source license.
#
# Modifications Copyright OpenSearch Contributors. See
# GitHub history for details.
#
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


from .utils import SKIP_IN_PATH, NamespacedClient, _make_path, query_params


class IngestClient(NamespacedClient):
    @query_params("leader_timeout", "summary")
    def get_pipeline(self, id=None, params=None, headers=None):
        """
        Returns a pipeline.


        :arg id: Comma separated list of pipeline ids. Wildcards
            supported
        :arg leader_timeout: Explicit operation timeout for connection
            to leader node
        :arg summary: Return pipelines without their definitions
            (default: false)
        """
        return self.transport.perform_request(
            "GET", _make_path("_ingest", "pipeline", id), params=params, headers=headers
        )

    @query_params("leader_timeout", "timeout")
    def put_pipeline(self, id, body, params=None, headers=None):
        """
        Creates or updates a pipeline.


        :arg id: Pipeline ID
        :arg body: The ingest definition
        :arg leader_timeout: Explicit operation timeout for connection
            to leader node
        :arg timeout: Explicit operation timeout
        """
        for param in (id, body):
            if param in SKIP_IN_PATH:
                raise ValueError("Empty value passed for a required argument.")

        return self.transport.perform_request(
            "PUT",
            _make_path("_ingest", "pipeline", id),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params("leader_timeout", "timeout")
    def delete_pipeline(self, id, params=None, headers=None):
        """
        Deletes a pipeline.


        :arg id: Pipeline ID
        :arg leader_timeout: Explicit operation timeout for connection
            to leader node
        :arg timeout: Explicit operation timeout
        """
        if id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'id'.")

        return self.transport.perform_request(
            "DELETE",
            _make_path("_ingest", "pipeline", id),
            params=params,
            headers=headers,
        )

    @query_params("verbose")
    def simulate(self, body, id=None, params=None, headers=None):
        """
        Allows to simulate a pipeline with example documents.


        :arg body: The simulate definition
        :arg id: Pipeline ID
        :arg verbose: Verbose mode. Display data output for each
            processor in executed pipeline
        """
        if body in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'body'.")

        return self.transport.perform_request(
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

        """
        return self.transport.perform_request(
            "GET", "/_ingest/processor/grok", params=params, headers=headers
        )

    @query_params()
    def geo_ip_stats(self, params=None, headers=None):
        """
        Returns statistical information about geoip databases

        """
        return self.transport.perform_request(
            "GET", "/_ingest/geoip/stats", params=params, headers=headers
        )
    
