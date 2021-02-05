import numpy as np
import cv2
from tensorflow.keras.utils import to_categorical

angry    = imlist(". . .\Emotion Datasets\test\angry")
disgust  = imlist(". . .\Emotion Datasets\test\disgust")
fear     = imlist(". . .\Emotion Datasets\test\fear")
happy    = imlist(". . .\Emotion Datasets\test\happy")
neutral  = imlist(". . .\Emotion Datasets\test\neutral")
sad      = imlist(". . .\Emotion Datasets\test\sad")
surprise = imlist(". . .\Emotion Datasets\test\surprise")

imagest = []
for img in angryt:
    x = cv2.imread(img)
    x = cv2.cvtColor(x, cv2.COLOR_BGR2GRAY)
    imagest.append(x)
for img in disgustt:
    x = cv2.imread(img)
    x = cv2.cvtColor(x, cv2.COLOR_BGR2GRAY)
    imagest.append(x)
for img in feart:
    x = cv2.imread(img)
    x = cv2.cvtColor(x, cv2.COLOR_BGR2GRAY)
    imagest.append(x)
for img in happyt:
    x = cv2.imread(img)
    x = cv2.cvtColor(x, cv2.COLOR_BGR2GRAY)
    imagest.append(x)
for img in neutralt:
    x = cv2.imread(img)
    x = cv2.cvtColor(x, cv2.COLOR_BGR2GRAY)
    imagest.append(x)
for img in sadt:
    x = cv2.imread(img)

x_test = x_test.reshape(len(x_test), 48, 48, 1)
    x = cv2.cvtColor(x, cv2.COLOR_BGR2GRAY)
    imagest.append(x)
for img in surpriset:
    x = cv2.imread(img)
    x = cv2.cvtColor(x, cv2.COLOR_BGR2GRAY)
    imagest.append(x)
x_test = np.array(imagest)
x_test = x_test.reshape(len(x_test), 48, 48, 1)
x_test.shape

labelst = []
for i in range(len(angryt)):
    labelst.append(0)
for i in range(len(disgustt)):
    labelst.append(1)
for i in range(len(feart)):
    labelst.append(2)
for i in range(len(happyt)):
    labelst.append(3)
for i in range(len(neutralt)):
    labelst.append(4)
for i in range(len(sadt)):
    labelst.append(5)
for i in range(len(surpriset)):
    labelst.append(6)

y_test = to_categorical(labelst)
y_test.shape
