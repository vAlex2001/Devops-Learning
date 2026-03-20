from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import os
import datetime
import psycopg2

# Database Connection
def get_db_connection():
    try:
        conn = psycopg2.connect(
            host=os.environ.get('DB_HOST', 'db'),
            database=os.environ.get('DB_NAME', 'dashboard'),
            user=os.environ.get('DB_USER', 'alex'),
            password=os.environ.get('DB_PASSWORD', 'devops123')
        )
        return conn
    except Exception as e:
        print(f"Database connection failed: {e}", flush=True)
        return None

# Creates requests table if it does not exist
def init_db():
    conn = get_db_connection()
    if conn:
        cur = conn.cursor()
        cur.execute(''' 
            CREATE TABLE IF NOT EXISTS requests (
                    id SERIAL PRIMARY KEY,
                    path VARCHAR(100),
                    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )
        ''')
        conn.commit()
        cur.close()
        conn.close()
        print("Database initialized successfully")
    else:
        print("Running without database")

# Log request to database
def log_request(path):
    conn = get_db_connection()
    if conn:
        try:
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO requests (path) VALUES (%s)",
                (path,)
            )
            conn.commit()
            cur.close()
            conn.close()
            print(f"Request logged: {path}", flush=True)
        except Exception as e:
            print(f"Error logging request: {e}", flush=True)
    else:
        print("No database connection available", flush=True)

# Get total request count from database
def get_request_count():
    conn = get_db_connection()
    if conn:
        try:
            cur = conn.cursor()
            cur.execute("SELECT COUNT(*) FROM requests")
            count = cur.fetchone()[0]
            cur.close()
            conn.close()
            return count
        except Exception as e:
            print(f"Error getting count: {e}", flush=True)
            return 0
    return 0

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            if self.path == '/':
                print(f"Handling request for /", flush=True)
                try:
                    log_request('/')
                    count = get_request_count()
                except Exception as e:
                    print(f"Error in request handling: {e}", flush=True)
                    count = 0

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
                    <h2>Database</h2>
                    <p>Status: <span style="color: #00ff88;">Connected</span></p>
                    <p>Total Requests: <span style="color: #00d4ff;">{count}</span></p>
                    <h2>Built by</h2>
                    <p>Alex - Junior DevOps Engineer</p>
                </body>
                </html> 
                """.format(
                    hostname = os.uname().nodename,
                    time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    count = count
                )
                self.wfile.write(html.encode())
            
            elif self.path == '/health':
                count = get_request_count()
                db_status = "connected" if get_db_connection() else "disconnected"

                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                response = {
                    "status": "healthy",
                    "hostname": os.uname().nodename,
                    "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "database": db_status,
                    "total_requests": count
                }
                self.wfile.write(json.dumps(response).encode())
        except Exception as e:
            print(f"Request handler error: {e}", flush=True)
            try:
                self.send_response(500)
                self.end_headers()
                self.wfile.write(b"Internal server error")
            except:
                pass

def log_message(self, format, *args):
        print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] {args[0]}", flush=True)

if __name__ == '__main__':
    init_db()
    port = int(os.environ.get('PORT', 8080))
    server = HTTPServer(('0.0.0.0', port), Handler)
    print(f"Server running on port {port}")
    server.serve_forever()