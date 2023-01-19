import os
os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'

import cv2
import easyocr
import matplotlib.pyplot as plt
import numpy as np


img = cv2.imread('image/text.jpg')

reader = easyocr.Reader(['en'], gpu = False)

text_ = reader.readtext(img)

threshold = 0.25

for t_, t in enumerate(text_):
    print(t)

    bbox, text, score = t

    if score > threshold:

        cv2.rectangle(img, bbox[0], bbox[2], (0, 255, 0), 5)
        cv2.putText(img, text, bbox[0], cv2.FONT_HERSHEY_COMPLEX, 0.65, (255, 0, 0), 2)

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()