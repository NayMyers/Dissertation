from flask import Flask, request
from flask_restful import Api, Resource
from datetime import datetime, date
import re
app = Flask(__name__)
api = Api(app)

# APP_ROOT = os.path.dirname(os.path.abspath(__file__))

class HelloWorld(Resource):
    def post(self, name):
        return {"data": "Hello World POST " + name}

    def get(self, name):
        return {"data": "Hello World GET " + name}

class Image(Resource):
    def put(self):
        responseMessage = "Invalid Request"
        pngPat = r"\.png"
        jpgPat = r"\.jpg"

        now = datetime.now()
        today = date.today()
        currentDate = today.strftime("%y-%m-%d")
        currentTime = now.strftime("%H-%M-%S")

        sentImageName = request.form['imageName']
        sentImage = request.files['image']

        pngCheck = re.search(pngPat, sentImageName)
        jpgCheck = re.search(jpgPat, sentImageName)
        if pngCheck == None and jpgCheck == None:
            return{"data": "INVALID FILE FORMAT. ONLY jpg OR png"}

        filetype = sentImageName.split('.')[-1]
        sentImageFileName = currentDate + '-' + currentTime + '.' + filetype
        sentImage.save(sentImageFileName)
        return{"data": "IMAGE " + sentImageName + " UPLOADED"}

    def get(self, image):
        return{"data": "GET TEST SUCCESS " + image}

api.add_resource(HelloWorld, "/hello_world/<string:name>")
api.add_resource(Image, "/upload_image")
if __name__ == "__main__":
    app.run(debug=True)
