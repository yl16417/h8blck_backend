from flask import Flask
from flask_restful import Api
from request import PerspectiveHandler
app = Flask(__name__)
api = Api(app)

api.add_resource(PerspectiveHandler, "/analyse/<string:texts>")
if __name__ == "__main__":
  app.run()
