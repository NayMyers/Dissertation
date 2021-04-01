from flask import Flask, request
from flask_restful import Api, Resource
from datetime import datetime, date
import re
import tensorflow as tf
import keras
import numpy as np
import os
import json
from PIL import Image
from keras import layers
from keras.layers import Input, Add, Dense, Activation, ZeroPadding2D, BatchNormalization, Flatten, Conv2D, AveragePooling2D, MaxPooling2D, GlobalMaxPooling2D
from keras.models import Model, load_model
from keras.preprocessing import image
from keras.utils import layer_utils
from keras.utils.data_utils import get_file
from keras.applications.imagenet_utils import preprocess_input
from keras.utils.vis_utils import model_to_dot
from keras.utils import plot_model
from keras.initializers import glorot_uniform
from keras.preprocessing import image
app = Flask(__name__)
api = Api(app)

# APP_ROOT = os.path.dirname(os.path.abspath(__file__))
cwd = os.getcwd()
IMAGE_PATH = cwd + "\\00e909aa-e3ae-4558-9961-336bb0f35db3___JR_FrgE.S 8593_270deg.jpg"
MODEL_FILE_PATH = cwd + "\\pre_train_inception.h5"

class Model:
    def __init__(self, modelFilePath):
        self.model_path = modelFilePath
        self.model = load_model(self.model_path)
        with open('cropClasses.json', 'r') as f:
            self.cropClasses = json.load(f)

    def preprocess(self, imageFilePath):
        image = tf.keras.preprocessing.image.load_img(imageFilePath, target_size=(224,224), interpolation="nearest")
        image_array = input_arr = keras.preprocessing.image.img_to_array(image)
        input_array = np.array([image_array])
        return input_array

    def determineClass(self, predictionArray):
        return np.argmax(predictionArray,axis=1)

    def determineClassName(self, classNum):
        classNum = int(classNum)
        for key, value in self.cropClasses.items():
            if classNum == value:
                return key
        return "key doesn't exist"

    def infer(self, imageFilePath = None):
        image = self.preprocess(imageFilePath)
        return self.model.predict(image)

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
        cwd = os.getcwd()
        filePath = cwd + "/" + sentImageFileName

        results = model.infer(filePath)
        predictedClass = str(np.argmax(results))
        className = model.determineClassName(predictedClass)
        results = results[0] #the list of results are nested inside a list so one pops off the outer list
        results = results.tolist()
        jsonResults = json.dumps(results)

        return{
        "data": "IMAGE " + sentImageName + " UPLOADED",
        "results" : jsonResults,
        "classNo" : predictedClass,
        "className": className
          }

    def get(self, image):
        return{"data": "GET TEST SUCCESS " + image}

api.add_resource(HelloWorld, "/hello_world/<string:name>")
api.add_resource(Image, "/upload_image")

if __name__ == "__main__":
    cwd = os.getcwd()
    modelFilePath = cwd + "/" + "pre_train_inception.h5"
    model = Model(modelFilePath)
    app.run(debug=True)
