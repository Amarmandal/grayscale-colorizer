import os
from skimage.io import imsave
from skimage.color import rgb2lab, lab2rgb, rgb2gray
from tensorflow.keras.utils import img_to_array, array_to_img,load_img
import keras
import numpy as np


def use_model(filename):
    print(filename+"hello")
    model = keras.models.load_model('./../my_model/output_model')
    color_me = []
    test_dataset_loc = './static/uploads/'
    color_me.append(img_to_array(load_img(test_dataset_loc + '/' + filename, target_size=(256, 256))))
    color_me = np.array(color_me, dtype=float)
    color_me = rgb2lab(1.0/255*color_me)[:,:,:,0]
    color_me = color_me.reshape(color_me.shape+(1,))

    print(color_me.shape)

    # Test model
    output = model.predict(color_me)
    output = output * 128

    # Output colorizations
    for i in range(len(output)):
        cur = np.zeros((256, 256, 3))
        cur[:,:,0] = color_me[i][:,:,0]
        cur[:,:,1:] = output[i]
    imsave(f"./static/outputs/{filename}", lab2rgb(cur))

# use_model('unknown.png')