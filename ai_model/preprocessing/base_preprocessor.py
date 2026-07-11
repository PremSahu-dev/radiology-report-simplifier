import cv2
import numpy as np


class BasePreprocessor:

    def resize(self, image, size=(224, 224)):
        return cv2.resize(image, size)

    def normalize(self, image):

        image = image.astype(np.float32)

        image = (image - image.min()) / (image.max() - image.min())

        return image
