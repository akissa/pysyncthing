# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4
# pysyncthing Python bindings for Syncthing REST API
# Copyright (C) 2015 Andrew Colin Kissa <andrew@topdog.za.net>
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.
"""
pysyncthing: Tests
"""
import json
import unittest

from mock import patch

from pysyncthing import SyncthingClient
from pysyncthing.resource import ENDPOINTS


def fake_request(*args, **kwargs):
    """Request implementation for testing"""
    path = kwargs.get('path')
    if path == ENDPOINTS['version']['name']:
        return json.loads('{"os": "linux"}')


class SyncthingClientTestCase(unittest.TestCase):
    """Test case for the SyncthingClient methods."""

    def setUp(self):
        """Setup"""
        self.patcher = patch('pysyncthing.SyncthingClient.request',
                        fake_request)
        self.patcher.start()
        self.client = SyncthingClient('QWERTYUIOP')

    def tearDown(self):
        """Tear Down"""
        self.patcher.stop()

    def test_get_version(self):
        response = self.client.get_version()
        self.assertIn('os', response)

    def test_get_connections(self):
        pass

    def test_get_config(self):
        pass

    def test_get_insync(self):
        pass

    def test_get_errors(self):
        pass

    def test_get_discovery(self):
        pass

    def test_new_error(self):
        pass

    def test_clear_errors(self):
        pass

    def test_new_config(self):
        pass

    def test_restart(self):
        pass

    def test_reset(self):
        pass

    def test_shutdown(self):
        pass

    def test_get_upgrade(self):
        pass

    def test_upgrade(self):
        pass

    def test_get_status(self):
        pass

    def test_get_ping(self):
        pass

    def test_new_ping(self):
        pass

    def test_browse_databse(self):
        pass

    def test_get_completion(self):
        pass

    def test_get_file(self):
        pass

    def test_get_ignores(self):
        pass

    def test_new_ignores(self):
        pass

    def test_get_need(self):
        pass

    def test_assign_priority(self):
        pass

    def test_scan(self):
        pass

    def test_get_folder_status(self):
        pass

    def test_get_device_statistics(self):
        pass

    def test_get_folder_statistics(self):
        pass
