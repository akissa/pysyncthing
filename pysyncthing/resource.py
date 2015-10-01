# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4
# pysyncthing Python bindings for Syncthing REST API
# Copyright (C) 2015 Andrew Colin Kissa <andrew@topdog.za.net>
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.
"""
pysyncthing resources
"""
import json

from restkit import Resource

from pysyncthing.exceptions import PySyncthingError


ENDPOINTS = {
    # System endpoints
    "version": {"name": '/rest/system/version', "method": "GET"},
    "connections": {"name": '/rest/system/connections', "method": "GET"},
    "config": {
        "get": {"name": '/rest/system/config', "method": "GET"},
        "new": {"name": '/rest/system/config', "method": "POST"},
        "insync": {"name": '/rest/system/config/insync', "method": "GET"}
    },
    "system": {
        "restart": {"name": '/rest/system/restart', "method": "POST"},
        "reset": {"name": '/rest/system/reset', "method": "POST"},
        "shutdown": {"name": '/rest/system/shutdown', "method": "POST"},
        "ping": {"name": '/rest/system/ping', "method": "GET"},
        "upgrade": {"name": '/rest/system/upgrade', "method": "GET"},
        "do_upgrade": {"name": '/rest/system/upgrade', "method": "POST"},
        "status": {"name": '/rest/system/status', "method": "GET"},
    },
    "errors": {
        "get": {"name": '/rest/system/error', "method": "GET"},
        "new": {"name": '/rest/system/error', "method": "POST"},
        "clear": {"name": '/rest/system/error/clear', "method": "POST"}
    },
    "discovery": {
        "get": {"name": '/rest/system/discovery', "method": "GET"},
        "new": {"name": '/rest/system/discovery/hint', "method": "POST"}
    },
    # Database endpoints
    "db": {
        "browse": {"name": '/rest/db/browse', "method": "GET"},
        "completion": {"name": '/rest/db/completion', "method": "GET"},
        "file": {"name": '/rest/db/file', "method": "GET"},
        "ignores": {"name": '/rest/db/ignores', "method": "GET"},
        "new_ignores": {"name": '/rest/db/ignores', "method": "POST"},
        "need": {"name": '/rest/db/need', "method": "GET"},
        "prio": {"name": '/rest/db/prio', "method": "POST"},
        "scan": {"name": '/rest/db/scan', "method": "POST"},
        "status": {"name": '/rest/db/status', "method": "GET"},
    },
    # Statistics endpoints
    "stats": {
        "device": {"name": '/rest/stats/device', "method": "GET"},
        "folder": {"name": '/rest/stats/folder', "method": "GET"}
    }
}


# pylint: disable=too-many-public-methods
class SyncthingClient(Resource):
    """SyncthingClient class"""

    def __init__(self, api_key, api_url='https://127.0.0.1:8384', **kwargs):
        """Init"""
        super(SyncthingClient, self).__init__(api_url, ssl_version=3,
                                              **kwargs)
        self.api_key = api_key

    def _request_headers(self):
        """Return the required API headers"""
        return {'X-API-Key': self.api_key,
                'User-Agent': 'pysyncthing',
                'Content-Type': 'application/json'}

    def request(self, *args, **kwargs):
        """Make the request"""
        try:
            response = super(SyncthingClient, self).request(
                *args, headers=self._request_headers(), **kwargs)
        except BaseException, err:
            code = 520
            if hasattr(err, 'status_int'):
                code = err.status_int
            if hasattr(err, 'message'):
                message = err.message
            else:
                message = str(err)
            raise PySyncthingError(code, message)
        if response.status_int == 200:
            body = response.body_string()
            if not len(body):
                body = '{"code":%d,"message":"Completed successfully"}' % \
                    response.status_int
        else:
            raise PySyncthingError(code=response.status_int,
                                   message=response.body_string())
        return json.loads(body)

    def api_call(self, opts, body=None, **kwargs):
        """Setup the request"""
        if body:
            body = json.dumps(body)
        return self.request(opts['method'], path=opts['name'],
                            payload=body, **kwargs)

    # System
    def get_version(self):
        """Gets version"""
        return self.api_call(ENDPOINTS["version"])

    def get_connections(self):
        """Gets connections"""
        return self.api_call(ENDPOINTS["connections"])

    def get_config(self):
        """Gets config"""
        return self.api_call(ENDPOINTS["config"]["get"])

    def get_insync(self):
        """Gets config insync"""
        return self.api_call(ENDPOINTS["config"]["insync"])

    def get_errors(self):
        """Gets errors"""
        return self.api_call(ENDPOINTS["errors"]["get"])

    def get_discovery(self):
        """Gets discovery"""
        return self.api_call(ENDPOINTS["discovery"]["get"])

    def new_error(self, error_body):
        """Sets new error"""
        return self.api_call(ENDPOINTS["errors"]["new"], error_body)

    def clear_errors(self):
        """Clears errors"""
        return self.api_call(ENDPOINTS["errors"]["clear"])

    def new_config(self, config):
        """Sets new config"""
        return self.api_call(ENDPOINTS["config"]["new"], config)

    def restart(self):
        """Restarts"""
        return self.api_call(ENDPOINTS["system"]["restart"])

    def reset(self):
        """Resets"""
        return self.api_call(ENDPOINTS["system"]["reset"])

    def shutdown(self):
        """Shutdown"""
        return self.api_call(ENDPOINTS["system"]["shutdown"])

    def get_upgrade(self):
        """Checks if upgrades available"""
        return self.api_call(ENDPOINTS["system"]["upgrade"])

    def upgrade(self):
        """Performs upgrade"""
        return self.api_call(ENDPOINTS["system"]["do_upgrade"])

    def get_status(self):
        """Gets status"""
        return self.api_call(ENDPOINTS["system"]["status"])

    def get_ping(self):
        """Gets ping"""
        return self.api_call(ENDPOINTS["system"]["ping"])

    def new_ping(self):
        """Gets ping"""
        return self.get_ping()

    # Database
    def browse_databse(self, folder, level=False, prefix=False):
        """Browse Database"""
        params = {'folder': folder, 'level': level, 'prefix': prefix}
        return self.api_call(ENDPOINTS["db"]["browse"],
                             None, params_dict=params)

    def get_completion(self, device_id, folder):
        """Gets completion stats"""
        params = {'device': device_id, 'folder': folder}
        return self.api_call(ENDPOINTS["db"]["completion"],
                             None, params_dict=params)

    def get_file(self, filename):
        """Gets a file"""
        params = {'file': filename}
        return self.api_call(ENDPOINTS["db"]["file"],
                             None, params_dict=params)

    def get_ignores(self, folder):
        """Gets ignores"""
        params = {'folder': folder}
        return self.api_call(ENDPOINTS["db"]["ignores"],
                             None, params_dict=params)

    def new_ignores(self, folder, ignores):
        """Sets ignores"""
        params = {'folder': folder}
        return self.api_call(ENDPOINTS["db"]["new_ignores"],
                             ignores, params_dict=params)

    def get_need(self, folder):
        """Gets need"""
        params = {'folder': folder}
        return self.api_call(ENDPOINTS["db"]["need"],
                             None, params_dict=params)

    def assign_priority(self, folder, filename):
        """Assigns priority"""
        params = {'folder': folder, 'file': filename}
        return self.api_call(ENDPOINTS["db"]["prio"],
                             None, params_dict=params)

    def scan(self, folder, subfolder=False):
        """Scans Database"""
        params = {'folder': folder, 'sub': subfolder}
        return self.api_call(ENDPOINTS["db"]["scan"],
                             None, params_dict=params)

    def get_folder_status(self, folder):
        """Gets folder status"""
        params = {'folder': folder}
        return self.api_call(ENDPOINTS["db"]["status"],
                             None, params_dict=params)

    # Stats
    def get_device_statistics(self):
        """Gets device Statistics"""
        return self.api_call(ENDPOINTS["stats"]["device"])

    def get_folder_statistics(self):
        """Gets folder Statistics"""
        return self.api_call(ENDPOINTS["stats"]["folder"])
