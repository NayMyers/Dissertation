from flask import Flask
from flask_restful import Api, Resource, reqparse
import werkzeug
app = Flask(__name__)
api = Api(app)

# APP_ROOT = os.path.dirname(os.path.abspath(__file__))

image_upload_args = reqparse.RequestParser()
image_upload_args.add_argument("imageName", type=str, help="Send Image Name", required=True)
image_upload_args.add_argument("image", type=werkzeug.datastructures.FileStorage,
    location='image', help="Send Image")

class HelloWorld(Resource):
    def post(self, name):
        return {"data": "Hello World POST " + name}

    def get(self, name):
        return {"data": "Hello World GET " + name}

class Image(Resource):
    # def post(self, image):
    #     return{"data": "Image " + image}

    def get(self, image):
        return{"data": "GET TEST SUCCESS " + image}

    def put(self):
        args = image_upload_args.parse_args()
        print(args)
        # uploaded_image = args['image']
        # uploaded_image.save(args['imageName'])
        return{"data": "IMAGE " + args['imageName'] + " UPLOADED"}


api.add_resource(HelloWorld, "/hello_world/<string:name>")
api.add_resource(Image, "/upload_image")
if __name__ == "__main__":
    app.run(debug=True)
