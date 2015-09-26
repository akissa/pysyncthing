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
import os

from imp import load_source
from setuptools import setup, find_packages


def get_readme():
    """Generate long description"""
    pandoc = None
    for path in os.environ["PATH"].split(os.pathsep):
        path = path.strip('"')
        pandoc = os.path.join(path, 'pandoc')
        if os.path.isfile(pandoc) and os.access(pandoc, os.X_OK):
            break
    try:
        if pandoc:
            cmd = [pandoc, '-t', 'rst', 'README.md']
            long_description = os.popen(' '.join(cmd)).read()
        else:
            raise ValueError
    except BaseException:
        long_description = open("README.md").read()
    return long_description


def main():
    """Main"""
    version = load_source("version", os.path.join("pysyncthing", "version.py"))

    opts = dict(name="pysyncthing",
        version=version.__version__,
        description="Python bindings for Syncthing REST API",
        long_description=get_readme(),
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
            'Operating System :: OS Independent'],
            )
    setup(**opts)


if __name__ == "__main__":
    main()
