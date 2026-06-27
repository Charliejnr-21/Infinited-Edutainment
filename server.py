import http.server
import socketserver
import webbrowser
import os
import sys

PORT = 8000

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Add headers to prevent caching for smooth client preview development
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

def run_server():
    # Ensure we are serving from the directory containing this script
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    Handler = CustomHandler
    
    # Try to bind to port 8000, fallback to another port if busy
    try:
        with socketserver.TCPServer(("", PORT), Handler) as httpd:
            url = f"http://localhost:{PORT}"
            print(f"\n==================================================")
            print(f"🚀 InfinitEd Local Host Server is Active!")
            print(f"👉 Open your browser to preview: {url}")
            print(f"==================================================\n")
            print(f"Press Ctrl+C to stop the server.\n")
            
            # Attempt to automatically open the web browser for the client preview
            try:
                webbrowser.open(url)
            except Exception:
                pass
            
            httpd.serve_forever()
    except OSError as e:
        print(f"❌ Port {PORT} is currently in use. Try closing other running servers or run: python3 -m http.server 8080")
        sys.exit(1)

if __name__ == "__main__":
    try:
        run_server()
    except KeyboardInterrupt:
        print("\n🛑 Server stopped. Goodbye!")
