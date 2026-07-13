from ai_model.preprocessing.base_preprocessor import BasePreprocessor


class CTPreprocessor(BasePreprocessor):

    def process(self, image):

        image = self.normalize(image)

        image = self.resize(image)

        return image
