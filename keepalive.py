from http.server import SimpleHTTPRequestHandler, HTTPServer
PORT = 10000
server = HTTPServer(("0.0.0.0", PORT), SimpleHTTPRequestHandler)
server.serve_forever()
