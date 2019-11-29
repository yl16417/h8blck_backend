from flask import Flask, request
from flask_restful import Api, Resource
import ast
import perspective


class PerspectiveHandler(Resource):
    def put(self):
        texts = request.form['data']
        textList = ast.literal_eval(texts)
        analysedTexts = perspective.processRequest(textList)
        print("Analysed text response is %s" % analysedTexts)
        return analysedTexts


app = Flask(__name__)
api = Api(app)
api.add_resource(PerspectiveHandler, *["/analyse/", "/analyse"])

if __name__ == "__main__":
    app.run(debug=True)
    

