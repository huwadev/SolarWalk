"""
Local Test Server for ESSS Solar Walk (including AR Camera Mode)
---------------------------------------------------------------
Browser Security Rule:
- Desktop PC / Laptops: 'http://localhost:8080' and 'http://127.0.0.1:8080'
  are automatically treated as SECURE CONTEXTS by Chrome, Edge, and Firefox.
  Camera (getUserMedia), GPS (Geolocation), and 3D WebGL run without any setup!

- Mobile Phones / Tablets over Wi-Fi:
  If accessing from your phone on the same Wi-Fi network (e.g. http://192.168.x.x:8080),
  you can either:
  Option A: Use ngrok or localtunnel for free instant HTTPS on your phone:
            npx localtunnel --port 8080
  Option B: In mobile Chrome, navigate to chrome://flags/#unsafely-treat-insecure-origin-as-secure
            and add your computer's IP (e.g. http://192.168.1.100:8080), then relaunch.
"""

import http.server
import socket
import socketserver
import os
import sys

PORT = 8080

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"

class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        super().end_headers()

def main():
    local_ip = get_local_ip()
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    print("=" * 68)
    print("  🚀 ESSS SOLAR WALK — LOCAL AR TEST SERVER")
    print("=" * 68)
    print(f"\n  [PC / Desktop Testing (Full Camera & AR Supported)]:")
    print(f"  👉 http://localhost:{PORT}/ESSS%20Solar%20Map.html")
    print(f"  👉 http://127.0.0.1:{PORT}/ESSS%20Solar%20Map.html")
    print(f"\n  [Phone / Tablet Testing over Wi-Fi]:")
    print(f"  👉 http://{local_ip}:{PORT}/ESSS%20Solar%20Map.html")
    print("\n  💡 Pro-Tip for Phones:")
    print("     Run in a separate terminal: npx localtunnel --port 8080")
    print("     This gives you a free, instant public HTTPS URL you can open on iOS/Android!")
    print("=" * 68)
    print("  Press Ctrl+C to stop the server.\n")

    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n  Server stopped.")

if __name__ == "__main__":
    main()
