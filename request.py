import http.server as s
import socketserver
from urllib import parse
from h8blck_backend import perspective

PORT = 9000


class PerspectiveHandler(s.BaseHTTPRequestHandler):
    def _set_headers(self):
        """
        Sets the headers for the request response
        """
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
    def _html(self, responseText):
        """
        Generate HTML response that includes responseText
        :param responseText: The text to include in response
        :return:
        """
        content = '<html><body><h1>{responseText}</h1></body></html>'
        return content.encode("utf8")
        
    def _parseRequestParameters(self):
        requestParameters = parse.urlsplit(self.path).query
        return dict(parse.parse_qs(requestParameters))
    
    def do_GET(self):
        self._set_headers()
        self.wfile.write(self._html('Received get request'))
        textList = self._parseRequestParameters()['texts']
        analysedTexts = perspective.processRequest(textList)
        self.wfile.write(self._html(analysedTexts))
        
        
with socketserver.TCPServer(("", PORT), PerspectiveHandler) as httpd:
    print('Server is up and running :O')
    httpd.serve_forever()
