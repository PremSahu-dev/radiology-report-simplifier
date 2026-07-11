from preprocessing.preprocess_xray import XRayPreprocessor
from preprocessing.preprocess_ct import CTPreprocessor
from preprocessing.preprocess_mri import MRIPreprocessor


class PreprocessingPipeline:

    def get_preprocessor(self, modality):

        modality = modality.upper()

        if modality in ["CR", "DX"]:
            return XRayPreprocessor()

        elif modality == "CT":
            return CTPreprocessor()

        elif modality == "MR":
            return MRIPreprocessor()

        else:
            raise ValueError("Unsupported modality")


""" 
from preprocessing.dicom_reader import DicomReader
from preprocessing.transforms import get_default_transform

from preprocessing.preprocess_xray import XRayPreprocessor
from preprocessing.preprocess_ct import CTPreprocessor
from preprocessing.preprocess_mri import MRIPreprocessor


class PreprocessingPipeline:

    def get_preprocessor(self, modality):

        modality = modality.upper()

        if modality in ["CR", "DX"]:
            return XRayPreprocessor()

        elif modality == "CT":
            return CTPreprocessor()

        elif modality == "MR":
            return MRIPreprocessor()

        else:
            raise ValueError("Unsupported modality")

    def process(self, dicom_path):

        # Read the DICOM file
        reader = DicomReader(dicom_path)
        reader.load()

        # Get pixel data and metadata
        image = reader.get_image()
        metadata = reader.get_metadata()

        # Select the correct preprocessor
        processor = self.get_preprocessor(metadata["modality"])

        # Apply preprocessing
        image = processor.process(image)

        # Apply PyTorch transforms
        transform = get_default_transform()
        image = transform(image)

        return image, metadata """
