#!/usr/bin/env python3
import http.server
import mimetypes

class FramerHandler(http.server.SimpleHTTPRequestHandler):
    def guess_type(self, path):
        mime, _ = mimetypes.guess_type(path)
        if mime is None:
            mime = "text/html"
        return mime

if __name__ == "__main__":
    import socketserver
    PORT = 8081
    with socketserver.TCPServer(("", PORT), FramerHandler) as httpd:
        print(f"Serving at http://localhost:{PORT}")
        httpd.serve_forever()
