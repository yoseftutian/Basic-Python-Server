from http.server import HTTPServer, BaseHTTPRequestHandler
import os
import mimetypes

class SimpleHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/" or self.path == "/index":
            self.serve_file("templates/index.html")
        else:
            # Static file handling
            file_path = self.path.lstrip("/")
            self.serve_file(file_path)

    def serve_file(self, file_path):
        if not os.path.exists(file_path):
            self.send_error(404, "File Not Found")
            return

        # Detect content type automatically
        content_type, _ = mimetypes.guess_type(file_path)
        content_type = content_type or "application/octet-stream"

        with open(file_path, "rb") as f:
            content = f.read()

        self.send_response(200)
        self.send_header("Content-Type", content_type)
        self.end_headers()
        self.wfile.write(content)

    def log_message(self, format, *args):
        return  # Disable noisy logging


def run_server(port=8000):
    server = HTTPServer(("localhost", port), SimpleHandler)
    print(f"[START] Server is running at http://localhost:{port}")
    server.serve_forever()


if __name__ == "__main__":
    run_server()
