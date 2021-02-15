from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

# APP_ROOT = os.path.dirname(os.path.abspath(__file__))

class HelloWorld(Resource):
    def get(self, name):
        return {"data": "Hello World " + name}

class Image(Resource):
    def post(self, image):
        return{"data": "TEST SUCCESS " + image}

    def get(self, image):
        return{"data": "GET TEST SUCCESS " + image}


api.add_resource(HelloWorld, "/hello_world/<string:name>")
api.add_resource(Image, "/upload_image/<string:image>")
if __name__ == "__main__":
    app.run(debug=True)
