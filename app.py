from flask import Flask
from flask_restful import Api
from request import PerspectiveHandler

app = Flask(__name__)
api = Api(app)

@app.route('/analyse', method = ['GET','POST'])
def analyse():
	data = request.get_json()
	handler = PerspectiveHandler()
	handler.get(data)

	return handler._html

api.add_resource(PerspectiveHandler, "/analyse/<string:texts>")
if __name__ == "__main__":
  app.run()
