#!/usr/bin/env python3

import http
from http.server import HTTPServer, BaseHTTPRequestHandler
import socketserver

class GetHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        msg = b'haahah'
        self.wfile.write(msg)
        return


PORT = 11123
httpd = socketserver.TCPServer(("", PORT), GetHandler)
print("serving at ", PORT)
httpd.serve_forever()


