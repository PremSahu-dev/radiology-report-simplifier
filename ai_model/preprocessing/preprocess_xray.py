from preprocessing.base_preprocessor import BasePreprocessor


class XRayPreprocessor(BasePreprocessor):

    def process(self, image):

        image = self.normalize(image)

        image = self.resize(image)

        return image
