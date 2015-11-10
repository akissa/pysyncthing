Usage
=====

**Parameters**

+------------+----------+--------------------------------------------------------+--------------+
| Name       | Type     | Description                                            | Mandatory?   |
+============+==========+========================================================+==============+
| api\_key   | string   | API key                                                | Yes          |
+------------+----------+--------------------------------------------------------+--------------+
| api\_url   | string   | Url to connect to. Default is https://127.0.0.1:8384   | No           |
+------------+----------+--------------------------------------------------------+--------------+

Make a new instance of SyncthingClient with API key and Url.

.. code:: python

    >> from pysyncthing import SyncthingClient
    >> client = SyncthingClient('XX6406JTI3NH673QRHOGU840PL8702', 'https://192.168.1.26:8384')

get\_version()
--------------

returns current version

.. code:: python

    >> client.get_version()

Response:

.. code:: json

    {'arch': 'amd64',
    'codename': 'Aluminium Ant',
    'longVersion': 'syncthing v0.11.25 "Aluminium Ant" (go1.4.2 linux-amd64 default) mockbuild@build2.home.topdog-software.com 2015-10-01 13:56:48 UTC',
    'os': 'linux',
    'version': 'v0.11.25'}

get\_connections()
------------------

Returns current connections

.. code:: python

    >> client.get_connections()

Response:

.. code:: json

    {'connections': {},
    'total': {'address': '',
        'at': '2015-11-10T09:47:04.702349573+02:00',
        'clientVersion': '',
        'inBytesTotal': 0,
        'outBytesTotal': 0}}

get\_config()
-------------

Returns current syncthing config

.. code:: python

    >> client.get_connections()

Response:

.. code:: json

    {'devices': [{'addresses': ['dynamic'],
               'certName': '',
               'compression': 'metadata',
               'deviceID': 'KIQNIU2-FCDVMLH-UOHLLDI-7XYZRDU-TPEQSW4-B4W3YTF-LWUJP3N-6SMUFFK',
               'introducer': False,
               'name': 'standalone.home.topdog-software.com'}],
    'folders': [{'autoNormalize': True,
               'copiers': 0,
               'devices': [{'deviceID': 'KIQNIU2-FCDVMLH-UOHLLDI-7XYZRDU-TPEQSW4-B4W3YTF-LWUJP3N-6SMUFFK'}],
               'hashers': 0,
               'id': 'ms-quarantine',
               'ignoreDelete': False,
               'ignorePerms': False,
               'invalid': '',
               'minDiskFreePct': 1,
               'order': 'random',
               'path': '/var/spool/MailScanner/quarantine',
               'pullers': 0,
               'readOnly': False,
               'rescanIntervalS': 60,
               'versioning': {'params': {}, 'type': ''}}],
    'gui': {'address': '0.0.0.0:8384',
          'apiKey': 'C1CrL0g-GZSD9galtsad6gl6pXOhk665',
          'enabled': True,
          'password': '',
          'useTLS': True,
          'user': ''},
    'ignoredDevices': [],
    'options': {'autoUpgradeIntervalH': 12,
              'cacheIgnoredFiles': True,
              'databaseBlockCacheMiB': 0,
              'globalAnnounceEnabled': False,
              'globalAnnounceServers': ['udp4://announce.syncthing.net:22026',
                                         'udp6://announce-v6.syncthing.net:22026'],
              'keepTemporariesH': 24,
              'limitBandwidthInLan': False,
              'listenAddress': ['0.0.0.0:1027'],
              'localAnnounceEnabled': False,
              'localAnnounceMCAddr': '[ff32::5222]:21026',
              'localAnnouncePort': 21025,
              'maxRecvKbps': 0,
              'maxSendKbps': 0,
              'minHomeDiskFreePct': 1,
              'pingIdleTimeS': 60,
              'pingTimeoutS': 30,
              'progressUpdateIntervalS': 5,
              'reconnectionIntervalS': 60,
              'restartOnWakeup': True,
              'startBrowser': False,
              'symlinksEnabled': True,
              'upnpEnabled': False,
              'upnpLeaseMinutes': 60,
              'upnpRenewalMinutes': 30,
              'upnpTimeoutSeconds': 10,
              'urAccepted': -1,
              'urUniqueId': ''},
    'version': 11}

get\_insync()
-------------

Returns current insync condition

.. code:: python

    >> client.get_insync()

Response:

.. code:: json

    {'configInSync': True}

get\_errors()
-------------

Returns raised and not cleared errors

.. code:: python

    >> client.get_errors()

Response:

.. code:: json

    {'errors': []}

get\_discovery()
----------------

Returns local discovery hash

.. code:: python

    >> client.get_discovery()

Response:

.. code:: json

    {}

new\_error()
------------

Raises a new error with given message. Returns code 200 on success.

.. code:: python

    >> client.new_error('foo')

Response:

.. code:: json

    {'message': 'Completed successfully', 'code': 200}

clear\_errors()
---------------

Clears previously raised errors. Returns code 200 on success.

.. code:: python

    >> client.clear_errors()

Response:

.. code:: json

    {'message': 'Completed successfully', 'code': 200}

new\_config()
-------------

Uploads a new config to syncthing server.

**Parameters**

+----------+--------+------------------------+--------------+
| Name     | Type   | Description            | Mandatory?   |
+==========+========+========================+==============+
| config   | Dict   | New syncthing config   | Yes          |
+----------+--------+------------------------+--------------+

.. code:: python

    cfg = {}
    >> client.new_config(cfg)

Response:

.. code:: json

    {'message': 'Completed successfully', 'code': 200}

restart()
---------

Will restart syncthing server

.. code:: python

    >> client.restart()

Response:

.. code:: json

    {'ok': 'restarting'}

reset()
-------

This means renaming all repository directories to temporary, unique
names, destroying all indexes and restarting.

This should probably not be used during normal operations...

.. code:: python

    >> client.reset()

Response:

.. code:: json

    {'ok': 'resetting database'}

shutdown()
----------

This shuts down the server

.. code:: python

    >> client.shutdown()

Response:

.. code:: json

    {'ok': 'shutting down'}

get\_upgrade()
--------------

Check for the new version

.. code:: python

    >> client.get_upgrade()

upgrade()
---------

Perform an upgrade and restart if new version exists. Does nothing if
current version is latest.

.. code:: python

    >> client.upgrade()

Response:

.. code:: json

    {'message': 'Completed successfully', 'code': 200}

get\_status()
-------------

Returns current status

.. code:: python

    >> client.get_status()

Response:

.. code:: json

    {'alloc': 8319640,
    'cpuPercent': 0.0399951236269495,
    'goroutines': 34,
    'myID': 'KIQNIU2-FCDVMLH-UOHLLDI-7XYZRDU-TPEQSW4-B4W3YTF-LWUJP3N-6SMUFFK',
    'pathSeparator': '/',
    'sys': 16267512,
    'tilde': '/var/spool/exim',
    'uptime': 752}

get\_ping()
-----------

Returns a ``{"ping": "pong"}`` object

.. code:: python

    >> client.get_ping()

Response:

.. code:: json

    {'ping': 'pong'}

browse\_databse()
------------------

**Parameters**

+----------+----------+-----------------------------------------------------+--------------+
| Name     | Type     | Description                                         | Mandatory?   |
+==========+==========+=====================================================+==============+
| folder   | string   | Name of a database                                  | Yes          |
+----------+----------+-----------------------------------------------------+--------------+
| level    | int      | Depth of a list. Default is ``0`` - maximum depth   | No           |
+----------+----------+-----------------------------------------------------+--------------+
| prefix   | string   | Path to directory or subdirectory to start from     | No           |
+----------+----------+-----------------------------------------------------+--------------+

Returns files in given folder

.. code:: python

    >> client.browse_databse('ms-quarantine')

Response:

.. code:: json

    {'phishingupdate': {'cache': {'2092': ['2015-08-06T16:08:26+02:00',
                                          252661],
                                '2092.42': ['2015-08-08T09:10:49+02:00',
                                             248535]},
                     'status': ['2015-08-08T09:10:49+02:00', 8]}}

get\_completion()
-----------------

Returns completion in percentage (0-100) for given device and folder

**Parameters**

+----------+----------+---------------+--------------+
| Name     | Type     | Description   | Mandatory?   |
+==========+==========+===============+==============+
| device   | string   | device\_id    | Yes          |
+----------+----------+---------------+--------------+
| folder   | string   | folder name   | Yes          |
+----------+----------+---------------+--------------+

.. code:: python

    >> client.get_completion('6RBLNBN-6EIGPRG-ZLZR7XI-LDWUXSE-NYWEBLI-3DFE2AI-L2DP3JL-4R77ZAM', 'ms-quarantine')

Response:

.. code:: json

    {'completion': 100}

get\_file()
-----------

Returns info for given file

**Parameters**

+--------+----------+---------------+--------------+
| Name   | Type     | Description   | Mandatory?   |
+========+==========+===============+==============+
| file   | string   | file name     | Yes          |
+--------+----------+---------------+--------------+

.. code:: python

    >> client.get_file('phishingupdate')

Response:

.. code:: json

    {'availability': None,
    'global': {'flags': '0',
             'localVersion': 0,
             'modified': '1970-01-01T02:00:00+02:00',
             'name': '',
             'numBlocks': 0,
             'size': 0,
             'version': []},
    'local': {'flags': '0',
            'localVersion': 0,
            'modified': '1970-01-01T02:00:00+02:00',
            'name': '',
            'numBlocks': 0,
            'size': 0,
            'version': []}}

get\_ignores()
--------------

Returns ignores for given folder

**Parameters**

+----------+----------+---------------+--------------+
| Name     | Type     | Description   | Mandatory?   |
+==========+==========+===============+==============+
| folder   | string   | folder        | Yes          |
+----------+----------+---------------+--------------+

.. code:: python

    >> client.get_ignores('ms-quarantine')

Response:

.. code:: json

    {'ignore': None, 'patterns': None}

new\_ignores()
--------------

Sets new ignores for given folder

**Parameters**

+-----------+----------+--------------------------------------------------+--------------+
| Name      | Type     | Description                                      | Mandatory?   |
+===========+==========+==================================================+==============+
| folder    | string   | folder                                           | Yes          |
+-----------+----------+--------------------------------------------------+--------------+
| ignores   | object   | ignore object like in ``get_ignores`` response   | Yes          |
+-----------+----------+--------------------------------------------------+--------------+

.. code:: python

    >> ignores = {'ignore': ['foo']}
    >> client.new_ignores('ms-quarantine', ignores)

Response:

.. code:: json

    {'ignore': ['foo'], 'patterns': ['^foo$', '^.*/foo$', '^foo/.*$', '^.*/foo/.*$']}

need()
------

Returns files which are needed for this device.

**Parameters**

+----------+----------+---------------+--------------+
| Name     | Type     | Description   | Mandatory?   |
+==========+==========+===============+==============+
| folder   | string   | folder        | Yes          |
+----------+----------+---------------+--------------+

.. code:: python

    >> client.get_need('ms-quarantine')

Response:

.. code:: json

    {'perpage': 65536, 'rest': [], 'queued': [], 'progress': [], 'total': 0, 'page': 1}

assign\_priority()
------------------

Assigns top priority for a given file in a given folder

**Parameters**

+----------+----------+---------------+--------------+
| Name     | Type     | Description   | Mandatory?   |
+==========+==========+===============+==============+
| folder   | string   | folder        | Yes          |
+----------+----------+---------------+--------------+
| file     | string   | filename      | Yes          |
+----------+----------+---------------+--------------+

.. code:: python

    >> client.assign_priority('ms-quarantine', '1Ze9NH-00057p-Vl')

Response:

.. code:: json

    {'perpage': 65536, 'rest': [], 'queued': [], 'progress': [], 'total': 0, 'page': 1}

scan()
------

Request an immediate rescan of a folder with a subfolder

**Parameters**

+-------------+----------+------------------+--------------+
| Name        | Type     | Description      | Mandatory?   |
+=============+==========+==================+==============+
| folder      | string   | folder           | Yes          |
+-------------+----------+------------------+--------------+
| subfolder   | string   | subfolder name   | No           |
+-------------+----------+------------------+--------------+

.. code:: python

    >> client.scan('ms-quarantine')

Response:

.. code:: json

    {'message': 'Completed successfully', 'code': 200}

get\_folder\_status()
---------------------

Returns status for a given folder

**Parameters**

+----------+----------+---------------+--------------+
| Name     | Type     | Description   | Mandatory?   |
+==========+==========+===============+==============+
| folder   | string   | folder        | Yes          |
+----------+----------+---------------+--------------+

.. code:: python

    >> client.get_folder_status('ms-quarantine')

Response:

.. code:: json

    {'globalBytes': 501460,
    'globalDeleted': 0,
    'globalFiles': 5,
    'ignorePatterns': True,
    'inSyncBytes': 501460,
    'inSyncFiles': 5,
    'invalid': '',
    'localBytes': 501460,
    'localDeleted': 0,
    'localFiles': 5,
    'needBytes': 0,
    'needFiles': 0,
    'state': 'idle',
    'stateChanged': '2015-11-10T10:03:28.992782938+02:00',
    'version': 6}

get\_device\_statistics()
-------------------------

Returns device statistics

.. code:: python

    >> client.get_device_statistics()

Response:

.. code:: json

    {'KIQNIU2-FCDVMLH-UOHLLDI-7XYZRDU-TPEQSW4-B4W3YTF-LWUJP3N-6SMUFFK': {'lastSeen': '1970-01-01T02:00:00+02:00'}}

get\_folder\_statistics()
-------------------------

Returns general statistics about folders.

.. code:: python

    >> client.get_folder_statistics()

Response:

.. code:: json

    {'ms-quarantine': {'lastFile': {'at': '0001-01-01T00:00:00Z',
                                  'deleted': False,
                                  'filename': ''}}}
