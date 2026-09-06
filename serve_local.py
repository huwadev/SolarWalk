import http.server
import socket
import socketserver
import os
import sys

# Force UTF-8 stdout if possible on Windows
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

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
    print("  ESSS SOLAR WALK - LOCAL AR TEST SERVER")
    print("=" * 68)
    print(f"\n  [PC / Desktop Testing (Full Camera & AR Supported)]:")
    print(f"  -> http://localhost:{PORT}/ESSS%20Solar%20Map.html")
    print(f"  -> http://127.0.0.1:{PORT}/ESSS%20Solar%20Map.html")
    print(f"\n  [Phone / Tablet Testing over Wi-Fi]:")
    print(f"  -> http://{local_ip}:{PORT}/ESSS%20Solar%20Map.html")
    print("\n  Tip for Mobile Phones:")
    print("     Run in a separate terminal: npx localtunnel --port 8080")
    print("     This creates an instant public HTTPS link for iOS/Android!")
    print("=" * 68)
    print("  Server is RUNNING. Press Ctrl+C to stop.\n")

    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n  Server stopped.")

if __name__ == "__main__":
    main()
