from flask import Flask, request
from flask_restful import Api, Resource
import perspective, json


class PerspectiveHandler(Resource):
    def put(self):
        textList = json.load(request.json)
        analysedTexts = perspective.processRequest(textList)
        return {'texts': analysedTexts}


app = Flask(__name__)
api = Api(app)
api.add_resource(PerspectiveHandler, *["/analyse/", "/analyse"])

if __name__ == "__main__":
    app.run(debug=True)
    

