#!/usr/bin/env python3
#
# Step two in building the messageboard server:
# A server that handles both GET and POST requests.
#
# Instructions:
#
# 1. Add a string variable that contains the form from Messageboard.html.
# 2. Add a do_GET method that returns the form.
#
# You don't need to change the do_POST method in this exercise!
#
# To test your code, run this server and access it at http://localhost:8000/
# in your browser.  You should see the form.  Then put a message into the
# form and submit it.  You should then see the message echoed back to you.

from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs

form = '''<!DOCTYPE html>
  <title>Message Board</title>
  <form method="POST" action="http://localhost:8000/">
    <textarea name="message"></textarea>
    <br>
    <button type="submit">Post it!</button>
  </form>
'''

class MessageHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        # 1. How long was the message? (Use the Content-Length header.)
        message_length = self.headers.get('Content-length', 0) #<-- Find length of message
        length = int(message_length) #<-- Convert that string to an int


        # 2. Read the correct amount of data from the request.
        request_data = self.rfile.read(length) #<-- Uses the self.rfile object and the read() method to read the request body
        data = request_data.decode() #<-- We now need to decode the result

        # 3. Extract the "message" field from the request data.
        message = parse_qs(data)["message"][0]

        print("Message Data:", data)
        print("Parsed message data:", message)

        # Send the "message" field back as the response.
        self.send_response(200)
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()
        self.wfile.write(message.encode())

    def do_GET(self):
        #Part 1 - sends send_response
        self.send_response(200)

        #Part 2 - send end_headers
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()

        #Part 3 - write the response body
        self.wfile.write(form.encode())

if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, MessageHandler)
    httpd.serve_forever()
