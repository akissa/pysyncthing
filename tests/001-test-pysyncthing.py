import t

from urlparse import urlparse

from _st import HOST, PORT
from pysyncthing.resource import ENDPOINTS
from pysyncthing.exceptions import PySyncthingError

BASE_URL = 'http://%s:%s' % (HOST, PORT)


@t.ApiRequest(url='http://127.0.0.1:8385')
def test_connect_error(api):
    t.raises(PySyncthingError, api.get_version)


@t.ApiRequest()
def test_get_version(api):
    resp = api.get_version()
    path = ENDPOINTS['version']['name']
    t.eq(api.response.final_url, '%s%s' % (BASE_URL, path))
    t.eq(api.response.request.method, ENDPOINTS['version']['method'])
    t.eq(api.response.status_int, 200)
    t.isin('os', resp)
    t.isin('version', resp)
    t.eq(resp['os'], 'linux')


@t.ApiRequest()
def test_get_connections(api):
    """Get connections"""
    resp = api.get_connections()
    path = ENDPOINTS["connections"]['name']
    t.eq(api.response.final_url, '%s%s' % (BASE_URL, path))
    t.eq(api.response.request.method, ENDPOINTS["connections"]['method'])
    t.eq(api.response.status_int, 200)
    t.isin('connections', resp)


@t.ApiRequest()
def test_get_config(api):
    """comments"""
    resp = api.get_config()
    path = ENDPOINTS["config"]["get"]['name']
    t.eq(api.response.final_url, '%s%s' % (BASE_URL, path))
    t.eq(api.response.request.method, ENDPOINTS["config"]["get"]['method'])
    t.eq(api.response.status_int, 200)
    t.isin('version', resp)


@t.ApiRequest()
def test_get_insync(api):
    """comments"""
    resp = api.get_insync()
    path = ENDPOINTS["config"]["insync"]['name']
    t.eq(api.response.final_url, '%s%s' % (BASE_URL, path))
    t.eq(api.response.request.method, ENDPOINTS["config"]["insync"]['method'])
    t.eq(api.response.status_int, 200)
    t.isin('configInSync', resp)


@t.ApiRequest()
def test_get_errors(api):
    """comments"""
    resp = api.get_errors()
    path = ENDPOINTS["errors"]["get"]['name']
    t.eq(api.response.final_url, '%s%s' % (BASE_URL, path))
    t.eq(api.response.request.method, ENDPOINTS["errors"]["get"]['method'])
    t.eq(api.response.status_int, 200)
    t.isin('errors', resp)


@t.ApiRequest()
def test_get_discovery(api):
    """comments"""
    resp = api.get_discovery()
    path = ENDPOINTS["discovery"]["get"]['name']
    t.eq(api.response.final_url, '%s%s' % (BASE_URL, path))
    t.eq(api.response.request.method, ENDPOINTS["discovery"]["get"]['method'])
    t.eq(api.response.status_int, 200)


@t.ApiRequest()
def test_new_error(api):
    """comments"""
    resp = api.new_error('foobar')
    path = ENDPOINTS["errors"]["new"]['name']
    t.eq(api.response.final_url, '%s%s' % (BASE_URL, path))
    t.eq(api.response.request.method, ENDPOINTS["errors"]["new"]['method'])
    t.eq(api.response.status_int, 200)
    t.isin('code', resp)
    t.eq(resp['code'], 200)


@t.ApiRequest()
def test_clear_errors(api):
    """comments"""
    resp = api.clear_errors()
    path = ENDPOINTS["errors"]["clear"]['name']
    t.eq(api.response.final_url, '%s%s' % (BASE_URL, path))
    t.eq(api.response.request.method, ENDPOINTS["errors"]["clear"]['method'])
    t.eq(api.response.status_int, 200)
    t.isin('code', resp)
    t.eq(resp['code'], 200)


@t.ApiRequest()
def test_new_config(api):
    """comments"""
    resp = api.new_config({})
    path = ENDPOINTS["config"]["new"]['name']
    t.eq(api.response.final_url, '%s%s' % (BASE_URL, path))
    t.eq(api.response.request.method, ENDPOINTS["config"]["new"]['method'])
    t.eq(api.response.status_int, 200)
    t.isin('code', resp)
    t.eq(resp['code'], 200)


@t.ApiRequest()
def test_restart(api):
    """comments"""
    resp = api.restart()
    path = ENDPOINTS["system"]["restart"]['name']
    t.eq(api.response.final_url, '%s%s' % (BASE_URL, path))
    t.eq(api.response.request.method, ENDPOINTS["system"]["restart"]['method'])
    t.eq(api.response.status_int, 200)
    t.isin('ok', resp)
    t.eq(resp['ok'], 'restarting')


@t.ApiRequest()
def test_reset(api):
    """comments"""
    resp = api.reset()
    path = ENDPOINTS["system"]["reset"]['name']
    t.eq(api.response.final_url, '%s%s' % (BASE_URL, path))
    t.eq(api.response.request.method, ENDPOINTS["system"]["reset"]['method'])
    t.eq(api.response.status_int, 200)
    t.isin('ok', resp)
    t.eq(resp['ok'], 'resetting database')


@t.ApiRequest()
def test_shutdown(api):
    """comments"""
    resp = api.shutdown()
    path = ENDPOINTS["system"]["shutdown"]['name']
    t.eq(api.response.final_url, '%s%s' % (BASE_URL, path))
    t.eq(
        api.response.request.method,
        ENDPOINTS["system"]["shutdown"]['method'])
    t.eq(api.response.status_int, 200)
    t.isin('ok', resp)
    t.eq(resp['ok'], 'shutting down')


@t.ApiRequest()
def test_get_upgrade(api):
    """comments"""
    resp = api.get_upgrade()
    path = ENDPOINTS["system"]["upgrade"]['name']
    t.eq(api.response.final_url, '%s%s' % (BASE_URL, path))
    t.eq(
        api.response.request.method,
        ENDPOINTS["system"]["upgrade"]['method'])
    t.eq(api.response.status_int, 200)


@t.ApiRequest()
def test_upgrade(api):
    """comments"""
    resp = api.upgrade()
    path = ENDPOINTS["system"]["do_upgrade"]['name']
    t.eq(api.response.final_url, '%s%s' % (BASE_URL, path))
    t.eq(
        api.response.request.method,
        ENDPOINTS["system"]["do_upgrade"]['method'])
    t.eq(api.response.status_int, 200)
    t.isin('code', resp)
    t.eq(resp['code'], 200)


@t.ApiRequest()
def test_get_status(api):
    """comments"""
    resp = api.get_status()
    path = ENDPOINTS["system"]["status"]['name']
    t.eq(api.response.final_url, '%s%s' % (BASE_URL, path))
    t.eq(
        api.response.request.method,
        ENDPOINTS["system"]["status"]['method'])
    t.eq(api.response.status_int, 200)
    t.isin('pathSeparator', resp)
    t.eq(resp['pathSeparator'], '/')


@t.ApiRequest()
def test_get_ping(api):
    """comments"""
    resp = api.get_ping()
    path = ENDPOINTS["system"]["ping"]['name']
    t.eq(api.response.final_url, '%s%s' % (BASE_URL, path))
    t.eq(
        api.response.request.method,
        ENDPOINTS["system"]["ping"]['method'])
    t.eq(api.response.status_int, 200)
    t.isin('ping', resp)
    t.eq(resp['ping'], 'pong')


@t.ApiRequest()
def test_new_ping(api):
    """comments"""
    resp = api.new_ping()
    path = ENDPOINTS["system"]["ping"]['name']
    t.eq(api.response.final_url, '%s%s' % (BASE_URL, path))
    t.eq(
        api.response.request.method,
        ENDPOINTS["system"]["ping"]['method'])
    t.eq(api.response.status_int, 200)
    t.isin('ping', resp)
    t.eq(resp['ping'], 'pong')


@t.ApiRequest()
def test_browse_databse(api):
    """comments"""
    resp = api.browse_databse('ms-quarantine')
    path = ENDPOINTS["db"]["browse"]['name']
    prd = urlparse(api.response.final_url)
    the_url = "%s://%s%s" % (prd.scheme, prd.netloc, prd.path)
    t.eq(the_url, '%s%s' % (BASE_URL, path))
    t.eq(
        api.response.request.method,
        ENDPOINTS["db"]["browse"]['method'])
    t.eq(api.response.status_int, 200)
    # t.isin('ping', resp)
    # t.eq(resp['ping'], 'pong')


@t.ApiRequest()
def test_get_completion(api):
    """comments"""
    devid = '6RBLNBN-6EIGPRG-ZLZR7XI-LDWUXSE-NYWEBLI-3DFE2AI-L2DP3JL-4R77ZAM'
    folder = 'ms-quarantine'
    resp = api.get_completion(devid, folder)
    path = ENDPOINTS["db"]["completion"]['name']
    prd = urlparse(api.response.final_url)
    the_url = "%s://%s%s" % (prd.scheme, prd.netloc, prd.path)
    t.eq(the_url, '%s%s' % (BASE_URL, path))
    t.eq(
        api.response.request.method,
        ENDPOINTS["db"]["completion"]['method'])
    t.eq(api.response.status_int, 200)
    t.isin('completion', resp)
    t.eq(resp['completion'], 0)


@t.ApiRequest()
def test_get_file(api):
    """comments"""
    resp = api.get_file('phishingupdate')
    path = ENDPOINTS["db"]["file"]['name']
    prd = urlparse(api.response.final_url)
    the_url = "%s://%s%s" % (prd.scheme, prd.netloc, prd.path)
    t.eq(the_url, '%s%s' % (BASE_URL, path))
    t.eq(
        api.response.request.method,
        ENDPOINTS["db"]["file"]['method'])
    t.eq(api.response.status_int, 200)
    t.isin('global', resp)


@t.ApiRequest()
def test_get_ignores(api):
    """comments"""
    folder = 'ms-quarantine'
    resp = api.get_ignores(folder)
    path = ENDPOINTS["db"]["ignores"]['name']
    prd = urlparse(api.response.final_url)
    the_url = "%s://%s%s" % (prd.scheme, prd.netloc, prd.path)
    t.eq(the_url, '%s%s' % (BASE_URL, path))
    t.eq(
        api.response.request.method,
        ENDPOINTS["db"]["ignores"]['method'])
    t.eq(api.response.status_int, 200)
    t.isin('patterns', resp)


@t.ApiRequest()
def test_new_ignores(api):
    """comments"""
    filename = '.git'
    folder = 'ms-quarantine'
    ignores = {'ignore': [filename]}
    resp = api.new_ignores(folder, ignores)
    path = ENDPOINTS["db"]["new_ignores"]['name']
    prd = urlparse(api.response.final_url)
    the_url = "%s://%s%s" % (prd.scheme, prd.netloc, prd.path)
    t.eq(the_url, '%s%s' % (BASE_URL, path))
    t.eq(
        api.response.request.method,
        ENDPOINTS["db"]["new_ignores"]['method'])
    t.eq(api.response.status_int, 200)
    t.isin('patterns', resp)
    t.isin('ignore', resp)
    t.eq("""["[u'%s']"]""" % filename, resp['ignore'])


@t.ApiRequest()
def test_get_need(api):
    """comments"""
    folder = 'ms-quarantine'
    resp = api.get_need(folder)
    path = ENDPOINTS["db"]["need"]['name']
    prd = urlparse(api.response.final_url)
    the_url = "%s://%s%s" % (prd.scheme, prd.netloc, prd.path)
    t.eq(the_url, '%s%s' % (BASE_URL, path))
    t.eq(
        api.response.request.method,
        ENDPOINTS["db"]["need"]['method'])
    t.eq(api.response.status_int, 200)
    t.isin('perpage', resp)
    t.isin('total', resp)


@t.ApiRequest()
def test_assign_priority(api):
    """comments"""
    folder = 'ms-quarantine'
    filename = 'phishingupdate'
    resp = api.assign_priority(folder, filename)
    path = ENDPOINTS["db"]["prio"]['name']
    prd = urlparse(api.response.final_url)
    the_url = "%s://%s%s" % (prd.scheme, prd.netloc, prd.path)
    t.eq(the_url, '%s%s' % (BASE_URL, path))
    t.eq(
        api.response.request.method,
        ENDPOINTS["db"]["prio"]['method'])
    t.eq(api.response.status_int, 200)
    t.isin('perpage', resp)
    t.isin('total', resp)


@t.ApiRequest()
def test_scan(api):
    """comments"""
    folder = 'ms-quarantine'
    resp = api.scan(folder)
    path = ENDPOINTS["db"]["scan"]['name']
    prd = urlparse(api.response.final_url)
    the_url = "%s://%s%s" % (prd.scheme, prd.netloc, prd.path)
    t.eq(the_url, '%s%s' % (BASE_URL, path))
    t.eq(
        api.response.request.method,
        ENDPOINTS["db"]["scan"]['method'])
    t.eq(api.response.status_int, 200)
    t.isin('code', resp)
    t.eq(resp['code'], 200)


@t.ApiRequest()
def test_get_folder_status(api):
    """comments"""
    folder = 'ms-quarantine'
    resp = api.get_folder_status(folder)
    path = ENDPOINTS["db"]["status"]['name']
    prd = urlparse(api.response.final_url)
    the_url = "%s://%s%s" % (prd.scheme, prd.netloc, prd.path)
    t.eq(the_url, '%s%s' % (BASE_URL, path))
    t.eq(
        api.response.request.method,
        ENDPOINTS["db"]["status"]['method'])
    t.eq(api.response.status_int, 200)
    t.isin('inSyncFiles', resp)
    t.isin('globalFiles', resp)


@t.ApiRequest()
def test_get_device_statistics(api):
    """comments"""
    resp = api.get_device_statistics()
    path = ENDPOINTS["stats"]["device"]['name']
    t.eq(api.response.final_url, '%s%s' % (BASE_URL, path))
    t.eq(
        api.response.request.method,
        ENDPOINTS["stats"]["device"]['method'])
    t.eq(api.response.status_int, 200)


@t.ApiRequest()
def test_get_folder_statistics(api):
    """comments"""
    resp = api.get_folder_statistics()
    path = ENDPOINTS["stats"]["folder"]['name']
    t.eq(api.response.final_url, '%s%s' % (BASE_URL, path))
    t.eq(
        api.response.request.method,
        ENDPOINTS["stats"]["folder"]['method'])
    t.eq(api.response.status_int, 200)
    t.isin('ms-quarantine', resp)
