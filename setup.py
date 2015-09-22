# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4
# pysyncthing Python bindings for Syncthing REST API
# Copyright (C) 2015 Andrew Colin Kissa <andrew@topdog.za.net>
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.
"""
pysyncthing: Python bindings for Syncthing REST API

Copyright 2015, Andrew Colin Kissa
Licensed under MPL 2.0.
"""
from setuptools import setup, find_packages


version = "0.0.1"

setup(name="pysyncthing",
      version=version,
      description="Python bindings for Syncthing REST API",
      long_description=open("README.md").read(),
      keywords="syncthing sync api rest backup syncronization",
      author="Andrew Colin Kissa",
      author_email="andrew@topdog.za.net",
      url="https://github.com/akissa/pysyncthing",
      license="MPL 2.0",
      packages=find_packages(exclude=['tests']),
      include_package_data=True,
      zip_safe=False,
      tests_require=['mock', 'nose'],
      install_requires=['restkit'],
      classifiers=[
            'Development Status :: 3 - Alpha',
            'Programming Language :: Python',
            'Programming Language :: Python :: 2.6',
            'Programming Language :: Python :: 2.7',
            'Topic :: Software Development :: Libraries :: Python Modules',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
            'Natural Language :: English',
            'Operating System :: OS Independent',
      ],
      )
