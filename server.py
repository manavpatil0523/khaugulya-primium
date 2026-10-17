import http.server
import socketserver
import webbrowser

PORT = 5500

class NoCacheHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
        super().end_headers()

print(f"🔥 Khaugulya 3D App running at: http://localhost:{PORT}")
print(f"🛠️ Admin Panel at: http://localhost:{PORT}/admin.html")
webbrowser.open(f"http://localhost:{PORT}")

with socketserver.TCPServer(("", PORT), NoCacheHandler) as httpd:
    httpd.serve_forever()