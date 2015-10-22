# -*- coding: utf-8 -
#
# Copyright (c) 2008 (c) Benoit Chesneau <benoitc@e-engura.com>
#
# Permission to use, copy, modify, and distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
"""HTTP test server"""
import json
import threading

from urllib import unquote
from urlparse import urlparse
from urlparse import parse_qsl
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

from restkit.util import to_bytestring


HOST = 'localhost'
PORT = 8384
TOKEN = '6e2347bc-278e-42f6-a84b-fa1766140cbd'


class HTTPTestHandler(BaseHTTPRequestHandler):
    """Testing handler"""
    def __init__(self, request, client_address, server):
        BaseHTTPRequestHandler.__init__(self, request, client_address, server)

    def _check_token(self):
        if 'X-API-Key' not in self.headers or \
                self.headers['X-API-Key'] != TOKEN:
            self.send_error(401)

    def do_GET(self):
        self._check_token()
        self.parsed_uri = urlparse(unquote(self.path))
        self.query = {}
        for key, val in parse_qsl(self.parsed_uri[4]):
            self.query[key] = val.decode('utf-8')
        path = self.parsed_uri[2]
        extra_headers = [('Content-type', 'application/json')]

        if path in [
            '/rest/stats/folder',
            '/rest/stats/device',
            '/rest/db/status',
            '/rest/db/need',
            '/rest/db/ignores',
            '/rest/db/file',
            '/rest/db/completion',
            '/rest/db/browse',
            '/rest/system/ping',
            '/rest/system/status',
            '/rest/system/upgrade',
            '/rest/system/discovery',
            '/rest/system/error',
            '/rest/system/config/insync',
            '/rest/system/config',
            '/rest/system/connections',
                '/rest/system/version']:
            with open('tests%s.json' % path) as handle:
                data = handle.read()
            self._respond(200, extra_headers, data)
        else:
            self._respond(404, [('Content-type', 'text/plain')], "Not Found")

    def do_POST(self):
        self._check_token()
        self.parsed_uri = urlparse(self.path)
        self.query = {}
        for key, val in parse_qsl(self.parsed_uri[4]):
            self.query[key] = val.decode('utf-8')
        path = self.parsed_uri[2]
        extra_headers = [('Content-type', 'application/json')]

        if path == '/rest/system/restart':
            resp = {'ok': 'restarting'}
            self._respond(200, extra_headers, json.dumps(resp))
        elif path == '/rest/system/reset':
            resp = {'ok': 'resetting database'}
            self._respond(200, extra_headers, json.dumps(resp))
        elif path == '/rest/system/shutdown':
            resp = {'ok': 'shutting down'}
            self._respond(200, extra_headers, json.dumps(resp))
        elif path == '/rest/db/ignores':
            content_length = int(self.headers.get('Content-length', 0))
            body = self.rfile.read(content_length)
            data = json.loads(body)
            tmpl = ('''["^\\%(ignore)s$","^.*/\\%(ignore)s$","^'''
                    '''\\%(ignore)s/.*$","^.*/\\%(ignore)s/.*$"]''')
            resp = {}
            resp['ignore'] = '["%(ignore)s"]' % data
            resp['patterns'] = tmpl % data
            self._respond(200, extra_headers, json.dumps(resp))
        elif path == '/rest/db/prio':
            resp = ("""{"page":1,"perpage":65536,"progress":[],"""
                    """"queued":[],"rest":[],"total":0}""")
            self._respond(200, extra_headers, resp)
        elif path in [
            '/api/v1/relays/1',
            '/api/v1/organizations',
            '/api/v1/radiussettings/1/2',
            '/rest/db/scan',
            '/rest/system/upgrade',
            '/rest/system/config',
            '/rest/system/error/clear',
                '/rest/system/error']:
            self._respond(200, extra_headers, "")
        else:
            self._respond(404, [('Content-type', 'text/plain')], "Not Found")

    def error_Response(self, message=None):
        req = [
            ('HTTP method', self.command),
            ('path', self.path),
            ]
        if message:
            req.append(('message', message))

        body_parts = ['Bad request:\r\n']
        for key, val in req:
            body_parts.append(' %s: %s\r\n' % (key, val))
        body = ''.join(body_parts)
        self._respond(
            400,
            [
                ('Content-type', 'text/plain'),
                ('Content-Length', str(len(body)))
            ],
            body)

    def _respond(self, http_code, extra_headers, body):
        self.send_response(http_code)
        keys = []
        for key, val in extra_headers:
            self.send_header(key, val)
            keys.append(key)
        if body:
            body = to_bytestring(body)
        self.end_headers()
        self.wfile.write(body)
        self.wfile.close()

    def finish(self):
        if not self.wfile.closed:
            self.wfile.flush()
        self.wfile.close()
        self.rfile.close()


server_thread = None


def run_server_test():
    global server_thread
    if server_thread is not None:
        return
    server = HTTPServer((HOST, PORT), HTTPTestHandler)
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.setDaemon(True)
    server_thread.start()
