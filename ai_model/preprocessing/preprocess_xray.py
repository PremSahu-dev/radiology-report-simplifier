import torchxrayvision as xrv

from preprocessing.base_preprocessor import BasePreprocessor


class XRayPreprocessor(BasePreprocessor):

    def process(self, image):

        # image is a NumPy array from DicomReader.pixel_array

        image = xrv.datasets.normalize(
            image,
            image.max()
        )

        image = image[None, :, :]

        image = xrv.datasets.XRayCenterCrop()(image)

        image = xrv.datasets.XRayResizer(224)(image)

        return image
