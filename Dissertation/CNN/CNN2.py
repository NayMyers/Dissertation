import tensorflow as tf
import keras
import numpy as np
import os
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

cwd = os.getcwd()
IMAGE_PATH = cwd + "\\00e909aa-e3ae-4558-9961-336bb0f35db3___JR_FrgE.S 8593_270deg.jpg"
MODEL_FILE_PATH = cwd + "\\pre_train_inception.h5"

class Model:
    def __init__(self, modelFilePath):
        self.model_path = modelFilePath
        self.model = load_model(self.model_path)

    def preprocess(self, imageFilePath):
        image = tf.keras.preprocessing.image.load_img(imageFilePath, target_size=(224,224), interpolation="nearest")
        image_array = input_arr = keras.preprocessing.image.img_to_array(image)
        input_array = np.array([image_array])
        return input_array

    def determineClass(self, predictionArray):
        return np.argmax(predictionArray,axis=1)
        
    def infer(self, imageFilePath = None):
        image = self.preprocess(imageFilePath)
        return self.model.predict(image)


model = Model(MODEL_FILE_PATH)
# image = np.asarray(Image.open(IMAGE_PATH).convert('RGB')).astype(np.float32)
# image = image[None, :, :, :]
imageFilePath = IMAGE_PATH


prediction = model.infer(imageFilePath)
print(prediction)
classes = np.argmax(prediction,axis=1)
print(classes)
print("END")
