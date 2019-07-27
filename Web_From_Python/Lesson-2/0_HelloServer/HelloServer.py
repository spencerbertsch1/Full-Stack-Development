#!/usr/bin/env python3
#
# The *hello server* is an HTTP server that responds to a GET request by
# sending back a friendly greeting.  Run this program in your terminal and
# access the server at http://localhost:8000 in your browser.

"""
Udacity Course - Full Stack Web Development
Summer 2019

This program uses the http.server python module to run a local web server to handle incoming HTTP requests until 
the program is stopped. 
"""
#Imports - we use HTTPServer and the BaseHTTPRequestHandler
from http.server import HTTPServer, BaseHTTPRequestHandler

# The HelloHandler class is a child class which inherits from the BaseHTTPRequestHandler class. 
# The one method: do_GET simply calls different methods from the parent class. 
class HelloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # First, send a 200 OK response.
        self.send_response(200)

        # Then send headers.
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()

        # Now, write the response body.
        self.wfile.write("Hello, HTTP!\n".encode())

if __name__ == '__main__':
    server_address = ('', 8000)  # Serve on all addresses, port 8000.
    httpd = HTTPServer(server_address, HelloHandler)
    httpd.serve_forever()
