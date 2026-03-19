from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import os
import datetime

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header('Content-type', ' text/html')
            self.end_headers()
            html = """
            <html>
            <head><title>DevOps Dashboard</title></head>
            <body style="font-family: Arial; padding: 40px; background: #1a1a2e; color: #eee;">
                <h1 style="color: #00d4ff;">DevOps Dashboard</h1>
                <h2>Server Info</h2>
                <p>Hostname: {hostname}</p>
                <p>Time: {time}</p>
                <p>Status: <span style="color: #00ff88;">Running</span></p>
                <h2>Built by</h2>
                <p>Alex - Junior DevOps Engineer</p>
            </body>
            </html>
            """.format(
                hostname = os.uname().nodename,
                time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            )
            self.wfile.write(html.encode())
        
        elif self.path == '/health':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = {
                "status": "healthy",
                "hostname": os.uname().nodename,
                "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            self.wfile.write(json.dumps(response).encode())

def log_message(self, format, *args):
    import sys
    print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] {args[0]}")


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    server = HTTPServer(('0.0.0.0', port), Handler)
    print(f"Server running on port {port}")
    server.serve_forever()