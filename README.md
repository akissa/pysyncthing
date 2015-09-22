# pysyncthing


## Python bindings for Syncthing REST API

This is a Python port of the [Ruby REST API Bindings](https://github.com/retgoat/syncthing-ruby)
for [Syncthing](http://syncthing.net/)

[![MPLv2 License](https://img.shields.io/badge/license-MPLv2-blue.svg?style=flat-square)](https://www.mozilla.org/MPL/2.0/)

## Installation

Install from PyPi

    pip install pysyncthing

Install from Githib

    git clone https://github.com/akissa/pysyncthing.git
    cd pysyncthing
    python setup.py install

## Usage


**Parameters**

|Name|Type|Description|Mandatory?|
|----|----|-----------|----------|
|api_key|string|API key|Yes|
|api_url|string|Url to connect to. Default is https://127.0.0.1:8384|No|

Make a new instance of SyncthingClient with API key and Url.

```python
>> c = SyncthingClient.new('XX6406JTI3NH673QRHOGU840PL8702', 'https://192.168.1.26:8384')
```

### get_version()

returns current version

```python
>> c.get_version()
{u'os': u'linux', u'codename': u'Aluminium Ant', u'version': u'v0.11.25', u'arch': u'amd64', u'longVersion': u'syncthing v0.11.25 "Aluminium Ant" (go1.4.2 linux-amd64 default) mockbuild@build2.home.topdog-software.com 2015-09-19 18:15:16 UTC'}
```

### get_connections()

Returns current connections

```python
>> c.get_connections()
{u'connections': {u'6RBLNBN-6EIGPRG-ZLZR7XI-LDWUXSE-NYWEBLI-3DFE2AI-L2DP3JL-4R77ZAM': {u'inBytesTotal': 40436, u'outBytesTotal': 43412, u'at': u'2015-09-22T23:10:31.182773186+02:00', u'clientVersion': u'v0.11.25', u'address': u'192.168.1.14:1027'}}, u'total': {u'inBytesTotal': 40436, u'outBytesTotal': 43412, u'at': u'2015-09-22T23:10:31.182824757+02:00', u'clientVersion': u'', u'address': u''}}
```

### get_config()

Returns current syncthing config

```python
>> c.get_config()
{u'folders': [{u'pullers': 0, u'hashers': 0, u'rescanIntervalS': 60, u'copiers': 0, u'devices': [{u'deviceID': u'UH3COQQ-AG2MDOF-YY7PBVX-M5T5FEQ-JIYZ57Q-C5PVKSW-3TVX7OT-MPNL6AD'}, {u'deviceID': u'6RBLNBN-6EIGPRG-ZLZR7XI-LDWUXSE-NYWEBLI-3DFE2AI-L2DP3JL-4R77ZAM'}], u'order': u'random', u'minDiskFreePct': 1, u'readOnly': False, u'ignoreDelete': False, u'invalid': u'', u'path': u'/var/spool/MailScanner/quarantine', u'autoNormalize': True, u'ignorePerms': False, u'id': u'ms-quarantine', u'versioning': {u'params': {}, u'type': u''}}], u'gui': {u'apiKey': u'8X2iXtByzNHJ4okYAzFELkd8vFNby8G5', u'enabled': True, u'useTLS': False, u'user': u'', u'address': u'192.168.1.26:8384', u'password': u''}, u'devices': [{u'compression': u'metadata', u'certName': u'', u'introducer': False, u'name': u'standalone.home.topdog-software.com', u'deviceID': u'UH3COQQ-AG2MDOF-YY7PBVX-M5T5FEQ-JIYZ57Q-C5PVKSW-3TVX7OT-MPNL6AD', u'addresses': [u'127.0.0.1:1027']}, {u'compression': u'metadata', u'certName': u'', u'introducer': False, u'name': u'ms2.home.topdog-software.com', u'deviceID': u'6RBLNBN-6EIGPRG-ZLZR7XI-LDWUXSE-NYWEBLI-3DFE2AI-L2DP3JL-4R77ZAM', u'addresses': [u'192.168.1.14:1027']}], u'version': 11, u'ignoredDevices': [], u'options': {u'urAccepted': -1, u'limitBandwidthInLan': False, u'upnpLeaseMinutes': 60, u'globalAnnounceServers': [u'udp4://announce.syncthing.net:22026', u'udp6://announce-v6.syncthing.net:22026'], u'upnpTimeoutSeconds': 10, u'pingTimeoutS': 30, u'localAnnounceMCAddr': u'[ff32::5222]:21026', u'maxSendKbps': 0, u'progressUpdateIntervalS': 5, u'autoUpgradeIntervalH': 12, u'maxRecvKbps': 0, u'keepTemporariesH': 24, u'listenAddress': [u'0.0.0.0:1027'], u'cacheIgnoredFiles': True, u'urUniqueId': u'', u'symlinksEnabled': True, u'globalAnnounceEnabled': False, u'localAnnounceEnabled': False, u'upnpRenewalMinutes': 30, u'pingIdleTimeS': 60, u'startBrowser': False, u'databaseBlockCacheMiB': 0, u'upnpEnabled': False, u'reconnectionIntervalS': 60, u'localAnnouncePort': 21025, u'restartOnWakeup': True, u'minHomeDiskFreePct': 1}}
```

### get_insync()

Returns current insync condition

```python
>> c.get_insync()
{u'configInSync': True}
```

### get_errors()

Returns raised and not cleared errors

```python
>> c.get_errors()
{u'errors': []}
```

### get_discovery()

Returns local discovery hash

```python
>> c.get_discovery()
=> {}
```

### new_error()

Raises a new error with given message. Returns code 200 on success.

```python
>> c.new_error('foo')
{u'message': u'Completed successfully', u'code': 200}
```

### clear_errors()

Clears previously raised errors. Returns code 200 on success.

```python
>> c.clear_errors()
{u'message': u'Completed successfully', u'code': 200}
```

### new_config()

Uploads a new config to syncthing server.

**Parameters**

|Name|Type|Description|Mandatory?|
|----|----|-----------|----------|
|config|Dict|New syncthing config|Yes|


```python
cfg = {}
>> c.new_config(cfg)
{u'message': u'Completed successfully', u'code': 200}
```

### restart()

Will restart syncthing server

```python
>> c.restart()
{u'ok': u'restarting'}
```

### reset()

This means renaming all repository directories to temporary, unique names,
destroying all indexes and restarting.

This should probably not be used during normal operations...

```python
>> c.reset()
{u'ok': 'resetting database'}
```

### shutdown()

```python
>> c.shutdown()
{u'ok': u'shutting down'}
```

### upgrade()

Check for the new veersion

```python
>> c.upgrade()
```

### upgrade()

Perform an upgrade and restart if new version exists. Does nothing if current
version is latest.

```python
>> c.upgrade()
{u'message': u'Completed successfully', u'code': 200}
```

### get_status()

Returns current status

```python
>> c.get_status()
{u'alloc': 10398664, u'cpuPercent': 0.02499997913651528, u'pathSeparator': u'/', u'uptime': 87, u'sys': 18495736, u'tilde': u'/var/spool/exim', u'myID': u'UH3COQQ-AG2MDOF-YY7PBVX-M5T5FEQ-JIYZ57Q-C5PVKSW-3TVX7OT-MPNL6AD', u'goroutines': 36}
```

### get_ping()

Returns a `{"ping": "pong"}` object

```python
>> c.get_ping()
{u'ping': u'pong'}
```

### browse_database()

**Parameters**

|Name|Type|Description|Mandatory?|
|----|----|-----------|----------|
|folder|string|Name of a database|Yes|
|level|int|Depth of a list. Default is `0` - maximum depth|No|
|prefix|string|Path to directory or subdirectory to start from|No|


Returns files in given folder

```python
>> c.browse_databse('ms-quarantine')
```

### get_completion()

Returns completion in percentage (0-100) for given device and folder

**Parameters**

|Name|Type|Description|Mandatory?|
|----|----|-----------|----------|
|device|string|device_id|Yes|
|folder|string|folder name|Yes|

```python
>> c.get_completion('6RBLNBN-6EIGPRG-ZLZR7XI-LDWUXSE-NYWEBLI-3DFE2AI-L2DP3JL-4R77ZAM', 'ms-quarantine')
{u'completion': 100}
```

### get_file()

Returns info for given file

**Parameters**

|Name|Type|Description|Mandatory?|
|----|----|-----------|----------|
|file|string|file name|Yes|


```python
>> c.get_file('1Ze9NH-00057p-Vl')
{u'global': {u'numBlocks': 0, u'name': u'', u'modified': u'1970-01-01T02:00:00+02:00', u'version': [], u'flags': u'0', u'localVersion': 0, u'size': 0}, u'local': {u'numBlocks': 0, u'name': u'', u'modified': u'1970-01-01T02:00:00+02:00', u'version': [], u'flags': u'0', u'localVersion': 0, u'size': 0}, u'availability': None}
```

### get_ignores()

Returns ignores for given folder

**Parameters**

|Name|Type|Description|Mandatory?|
|----|----|-----------|----------|
|folder|string|folder|Yes|


```python
>> c.get_ignores('ms-quarantine')
=> {u'ignore': None, u'patterns': None}
```

### new_ignores()

Sets new ignores for given folder

**Parameters**

|Name|Type|Description|Mandatory?|
|----|----|-----------|----------|
| folder |string|folder|Yes|
|ingores|object|ignore object like in `get_ignores` response|Yes|


```python
>> ignores = {'ignore': ['foo']}
>> c.new_ignores('ms-quarantine', ignores)
{u'ignore': [u'foo'], u'patterns': [u'^foo$', u'^.*/foo$', u'^foo/.*$', u'^.*/foo/.*$']}
```

### need()

Returns files which are needed for this device.

**Parameters**

|Name|Type|Description|Mandatory?|
|----|----|-----------|----------|
|folder|string|folder|Yes|


```python
>> c.get_need('ms-quarantine')
{u'perpage': 65536, u'rest': [], u'queued': [], u'progress': [], u'total': 0, u'page': 1}  
```

### assign_priority()

Assigns top priority for a given file in a given folder

**Parameters**

|Name|Type|Description|Mandatory?|
|----|----|-----------|----------|
|folder|string|folder|Yes|
|file|string|filename|Yes|


```python
>> c.assign_priority('ms-quarantine', '1Ze9NH-00057p-Vl')
{u'perpage': 65536, u'rest': [], u'queued': [], u'progress': [], u'total': 0, u'page': 1}
```

### scan()

Request an immediate rescan of a folder with a subfolder

**Parameters**

|Name|Type|Description|Mandatory?|
|----|----|-----------|----------|
|folder|string|folder|Yes|
|subfolder|string|subfolder name|No|


```python
>> c.scan('ms-quarantine')
{u'message': u'Completed successfully', u'code': 200}
```

### get_folder_status()

Returns status for a given folder

**Parameters**

|Name|Type|Description|Mandatory?|
|----|----|-----------|----------|
|folder|string|folder|Yes|


```python
>> c.get_folder_status('ms-quarantine')
{u'localBytes': 12115773, u'globalFiles': 514, u'needBytes': 0, u'ignorePatterns': True, u'localDeleted': 31, u'globalBytes': 12126909, u'invalid': u'', u'globalDeleted': 118, u'state': u'idle', u'version': 1835, u'inSyncFiles': 514, u'needFiles': 0, u'inSyncBytes': 12126909, u'localFiles': 514, u'stateChanged': u'2015-09-22T23:45:56.227948076+02:00'}
```

### get_device_statistics()

Returns device statistics

```python
>> c.get_device_statistics()
 {u'UH3COQQ-AG2MDOF-YY7PBVX-M5T5FEQ-JIYZ57Q-C5PVKSW-3TVX7OT-MPNL6AD': {u'lastSeen': u'1970-01-01T02:00:00+02:00'}, u'6RBLNBN-6EIGPRG-ZLZR7XI-LDWUXSE-NYWEBLI-3DFE2AI-L2DP3JL-4R77ZAM': {u'lastSeen': u'2015-09-22T23:47:03.851867821+02:00'}}
```

### get_folder_statistics()

Returns general statistics about folders.

```python
>> c.get_folder_statistics()
{u'ms-quarantine': {u'lastFile': {u'deleted': False, u'at': u'0001-01-01T00:00:00Z', u'filename': u''}}}
```


## Contributing

1. Fork it (https://github.com/akissa/pysyncthing/fork)
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create new Pull Request


## License

All code is licensed under the
[MPLv2 License](https://github.com/syncthing/syncthing/blob/master/LICENSE).
