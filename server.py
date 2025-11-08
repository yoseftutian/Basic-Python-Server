from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        
        html = """
        <!DOCTYPE html>
        <html dir="rtl" lang="he">
        <head>
            <meta charset="UTF-8">
            <title>השרת שלי</title>
        </head>
        <body>
            <h1>שלום! השרת עובד!</h1>
            <p>זהו שרת פייתון בסיסי 🚀</p>
        </body>
        </html>
        """
        self.wfile.write(html.encode('utf-8'))

PORT = 8000
server = HTTPServer(('localhost', PORT), SimpleHandler)

print(f'Serving on http://localhost:{PORT}')

server.serve_forever()