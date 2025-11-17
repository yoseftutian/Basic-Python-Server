from http.server import HTTPServer, BaseHTTPRequestHandler

HTML_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>My Server</title>
</head>
<body>
    <h1>Hello! The server is running!</h1>
    <p>This is a basic Python server 🚀</p>
</body>
</html>
"""

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print(f"[INFO] Request received from: {self.client_address}")

        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()

        self.wfile.write(HTML_PAGE.encode("utf-8"))

    def log_message(self, format, *args):
        return  # Disable default logging


def run_server(port=8000):
    server = HTTPServer(('localhost', port), SimpleHandler)
    print(f"[START] Server is running at http://localhost:{port}")
    server.serve_forever()


if __name__ == "__main__":
    run_server()
  