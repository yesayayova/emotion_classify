import os

def imlist(path):
    return [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.jpg')]
 
angry    = imlist(". . .\Emotion Datasets\train\angry")
disgust  = imlist(". . .\Emotion Datasets\train\disgust")
fear     = imlist(". . .\Emotion Datasets\train\fear")
happy    = imlist(". . .\Emotion Datasets\train\happy")
neutral  = imlist(". . .\Emotion Datasets\train\neutral")
sad      = imlist(". . .\Emotion Datasets\train\sad")
surprise = imlist(". . .\Emotion Datasets\train\surprise")

import numpy as np
import cv2

images = []

for img in angry:
    x = cv2.imread(img)
    x = cv2.cvtColor(x, cv2.COLOR_BGR2GRAY)
    images.append(x)

for img in disgust:
    x = cv2.imread(img)
    x = cv2.cvtColor(x, cv2.COLOR_BGR2GRAY)
    images.append(x)

for img in fear:
    x = cv2.imread(img)
    x = cv2.cvtColor(x, cv2.COLOR_BGR2GRAY)
    images.append(x)

for img in happy:
    x = cv2.imread(img)
    x = cv2.cvtColor(x, cv2.COLOR_BGR2GRAY)
    images.append(x)

for img in neutral:
    x = cv2.imread(img)
    x = cv2.cvtColor(x, cv2.COLOR_BGR2GRAY)
    images.append(x)

for img in sad:
    x = cv2.imread(img)
    x = cv2.cvtColor(x, cv2.COLOR_BGR2GRAY)
    images.append(x)

for img in surprise:
    x = cv2.imread(img)
    x = cv2.cvtColor(x, cv2.COLOR_BGR2GRAY)
    images.append(x)

x_train = np.array(images)
x_train.shape
