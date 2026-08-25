import http.server
import socketserver
import os

PORT = 3000

class CleanURLHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Remove query parameters and hashes for file matching
        path = self.path.split('?')[0].split('#')[0]
        
        # If requested path without extension matches a .html file, rewrite path
        if not path.endswith('.html') and not path.endswith('/'):
            local_html = os.path.join(os.getcwd(), path.lstrip('/') + '.html')
            if os.path.exists(local_html):
                self.path = path + '.html'
        
        return super().do_GET()

if __name__ == '__main__':
    # Allow port reuse immediately
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), CleanURLHandler) as httpd:
        print(f"DayForge server running at http://localhost:{PORT}")
        httpd.serve_forever()
