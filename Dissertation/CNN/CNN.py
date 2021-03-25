import tensorflow as tf
import keras
import os
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

cwd = os.getcwd()

MODEL_NAME = 'my_model'
VERSION = 1
MODEL_PATH = './my_model.h5'
SERVER_PATH = './server/{}/{}'.format(MODEL_NAME, VERSION)

PREDICT_INPUTS = "inputs"
PREDICT_METHOD_NAME = "tensorflow/serving/predits"
PREDICT_OUTPUTS = "outputs"

with tf.Session() as sess:
    model = tf.keras.models.load_model(MODEL_PATH, compile=True)
    graph = tf.get_default_graph()
    sess.run(tf.global_variables_initializer())
    inputs = graph.get_tensor_by_name('iputs:0')
    prediction = graph.get_tensor_by_name('predicitons/Sigmoid:0')
    model_input = tf.saved_model.utils.build_tensor_infor(inputs)
    model_output = tf.saved_model.utils.build_tensor_info(predictions)
    signature_def = tf.saved_model.signature_def_utils.build_signature_def(
    inputs={'inputs': model_input},
    outputs={'outputs': model_output},
    method_name = tf.saved_model.signature_constants.PREDICT_METHOD_NAME)

    builder = tf.saved_model.builder.SavedModelBuilder(SERVER_PATH)

    builder.add_meta_graph_and_variables(
    sess, [tf.saved_model.tag_constants.SERVING],
    signature_def_map={
        tf.saved_model.signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY:
            signature_definition
            }
        )
    builder.save()
