from pysyncthing import SyncthingClient


from _st import HOST, PORT, TOKEN, run_server_test
run_server_test()


class ApiRequest(object):

    def __init__(self, api_token=None, url=None, **client_opts):
        client_opts = client_opts or {}
        self.api_token = api_token or TOKEN
        self.client_opts = client_opts
        if url is not None:
            self.url = url
        else:
            self.url = 'http://%s:%s' % (HOST, PORT)

    def __call__(self, func):
        def run():
            res = SyncthingClient(self.api_token, self.url, **self.client_opts)
            func(res)
        run.func_name = func.func_name
        return run


def eq(a, b):
    assert a == b, "%r != %r" % (a, b)


def ne(a, b):
    assert a != b, "%r == %r" % (a, b)


def lt(a, b):
    assert a < b, "%r >= %r" % (a, b)


def gt(a, b):
    assert a > b, "%r <= %r" % (a, b)


def isin(a, b):
    assert a in b, "%r is not in %r" % (a, b)


def isnotin(a, b):
    assert a not in b, "%r is in %r" % (a, b)


def has(a, b):
    assert hasattr(a, b), "%r has no attribute %r" % (a, b)


def hasnot(a, b):
    assert not hasattr(a, b), "%r has an attribute %r" % (a, b)


def raises(exctype, func, *args, **kwargs):
    try:
        func(*args, **kwargs)
    except exctype:
        pass
    else:
        func_name = getattr(func, "func_name", "<builtin_function>")
        raise AssertionError("Function %s did not raise %s" % (
            func_name, exctype.__name__))
