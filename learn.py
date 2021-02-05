from PIL import Image
import numpy as np

def learn(img):
    img_arr = img.reshape(48, 48, 1)
    x = []
    x.append(img_arr)
    x = np.array(x)
    result = model.predict(x)
    label = ['angry  ','disgust','fear   ','happy  ','neutral','sad    ','surprise']

    return label, result
