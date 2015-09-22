# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4
# pysyncthing Python bindings for Syncthing REST API
# Copyright (C) 2015 Andrew Colin Kissa <andrew@topdog.za.net>
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.
"""
pysyncthing exceptions
"""


class PySyncthingError(Exception):
    """PySyncthing Exceptions"""
    def __init__(self, code, message):
        """Init"""
        super(PySyncthingError, self).__init__(message)
        self.code = code
