# Tools for a basic web server, built into Python
from http.server import HTTPServer, BaseHTTPRequestHandler

# A handler decides what to do when someone visits
class H(BaseHTTPRequestHandler):
    # do_GET runs every time a browser or curl asks for a page
    def do_GET(self):
        self.send_response(200)   # reply "OK"
        self.end_headers()        # end of the reply's header lines
        self.wfile.write(b"hello from V2\n")   # the text sent back

# Start the server on port 9999  and keep it running
# "0.0.0.0" means: accept visitors from outside the container
HTTPServer(("0.0.0.0", 8000 ), H).serve_forever()
