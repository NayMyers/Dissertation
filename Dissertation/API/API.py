from flask import Flask, request
from flask_restful import Api, Resource, reqparse
import base64
app = Flask(__name__)
api = Api(app)

# APP_ROOT = os.path.dirname(os.path.abspath(__file__))

image_upload_args = reqparse.RequestParser()

class HelloWorld(Resource):
    def post(self, name):
        return {"data": "Hello World POST " + name}

    def get(self, name):
        return {"data": "Hello World GET " + name}

class Image(Resource):
    def put(self):
        sentImage = request.files['image']
        sentImage.save('testImageName3.png')
        return{"data": "IMAGE " + 'sentimagename' + " UPLOADED"}

    def get(self, image):
        return{"data": "GET TEST SUCCESS " + image}

api.add_resource(HelloWorld, "/hello_world/<string:name>")
api.add_resource(Image, "/upload_image")
if __name__ == "__main__":
    app.run(debug=True)
