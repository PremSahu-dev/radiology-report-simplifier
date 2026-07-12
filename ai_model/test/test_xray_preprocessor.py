from preprocessing.dicom_reader import DicomReader
from preprocessing.preprocess_xray import XRayPreprocessor

reader = DicomReader(
    "/home/kali/Downloads/000001.dcm"
)

reader.load()

image = reader.get_image()

preprocessor = XRayPreprocessor()

processed = preprocessor.process(image)

print(type(processed))
print(processed.shape)
print(processed.dtype)
