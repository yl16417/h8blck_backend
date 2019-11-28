from flask import Flask, request
from flask_restful import Api, Resource
import perspective


class PerspectiveHandler(Resource):
    def get(self):
        texts = request.form['data']
        textList = texts.split(",")
        analysedTexts = perspective.processRequest(textList)
        return {'texts': analysedTexts}


app = Flask(__name__)
api = Api(app)
api.add_resource(PerspectiveHandler, *["/analyse/", "/analyse"])

if __name__ == "__main__":
    app.run(debug=True)
    

