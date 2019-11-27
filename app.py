from flask import Flask
from flask_restful import Api
from flask_restful import Resource
import perspective


class PerspectiveHandler(Resource):
    def get(self, texts):
        textList = texts.split(",")
        analysedTexts = perspective.processRequest(textList)
        return analysedTexts, 200


app = Flask(__name__)
api = Api(app)
api.add_resource(PerspectiveHandler, "/analyse/<string:texts>")

if __name__ == "__main__":
    app.run(debug=True)
    

