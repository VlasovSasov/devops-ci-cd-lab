"""
For Flask web server
"""

import http.server
import socketserver

PORT = 8000

class TestMe():
    """ Test class"""

    def take_five(self):
        """Return 5"""
        return 5

    def port(self):
        """Return port"""
        return PORT

if __name__ == '__main__':
    """Main.com"""
    Handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", PORT), Handler) as http:
        print("Port Vlasova: ", PORT)
        http.serve_forever()
