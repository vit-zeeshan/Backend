from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        message = f"Hello buddy from {self.server.service_name}!"
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(message.encode())

if __name__ == "__main__":
    import os
    service_name = os.getenv("SERVICE_NAME", "UnknownService")
    server = HTTPServer(('', 8088), SimpleHandler)
    server.service_name = service_name
    print(f"🚀 {service_name} running on http://localhost:8088")
    server.serve_forever()

