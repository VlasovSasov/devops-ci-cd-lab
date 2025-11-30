"""
For Flask web server
"""

import http.server
import socketserver

PORT = 8000

class TestMe():
    """ Dai 5!"""
    def take_five(self):
        return 5

    """ Nomer porta"""
    def port(self):
        return PORT

if __name__ == '__main__':
    """Main.com"""
    Handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", PORT), Handler) as http:
        print("Port Vlasova: ", PORT)
        http.serve_forever()
