from flask import request
from flask_restful import Resource
import perspective


class PerspectiveHandler(Resource):
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
        
    def _parseRequestParameters(self, texts):
        
        return []
    
    def get(self, texts):
        self._set_headers()
        self.wfile.write(self._html('Received get request'))
        textList = self._parseRequestParameters(texts)
        analysedTexts = perspective.processRequest(textList)
        self.wfile.write(self._html(analysedTexts))
