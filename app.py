from flask import Flask, request
from flask_restful import Api, Resource
import perspective, json


class PerspectiveHandler(Resource):
    def put(self):
        print(str(request.form))
        texts = request.form['data']
        analysedTexts = perspective.processRequest(texts)
        return {'texts': analysedTexts}


app = Flask(__name__)
api = Api(app)
api.add_resource(PerspectiveHandler, *["/analyse/", "/analyse"])

if __name__ == "__main__":
    app.run(debug=True)
    

