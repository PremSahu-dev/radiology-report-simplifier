import sys
import os

# Add the ai_model directory to Python's search path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from preprocessing.dicom_reader import DicomReader
from preprocessing.visualize import show_image







from preprocessing.pipeline import PreprocessingPipeline
from preprocessing.dicom_reader import DicomReader
import numpy as np

dicom_path = "/home/kali/Tproject/radiology-report-simplifier-main/ai_model/preprocessing/imgMR2.dcm"

reader = DicomReader(dicom_path)

reader.load()

metadata = reader.get_metadata()
image = reader.get_image()

print("Metadata:")
print(metadata)

pipeline = PreprocessingPipeline()

processor = pipeline.get_preprocessor(metadata["modality"])

processed_image = processor.process(image)

print("\nOriginal Image Shape:", image.shape)

pipeline = PreprocessingPipeline()

processor = pipeline.get_preprocessor(metadata["modality"])

print("\nSelected Preprocessor:", processor.__class__.__name__)

processed_image = processor.process(image)

print("Processed Image Shape:", processed_image.shape)

print("\nData Type:", image.dtype)

print("Minimum Pixel Value:", np.min(image))

print("Maximum Pixel Value:", np.max(image))

show_image(image, "Original MRI")









'''

from preprocessing.dicom_reader import DicomReader

# Replace with the path to your DICOM file
dicom_path = "/home/kali/Tproject/radiology-report-simplifier-main/ai_model/preprocessing/imgMR1.dcm"

reader = DicomReader(dicom_path)

# Load DICOM
reader.load()

# Extract metadata
metadata = reader.get_metadata()

print("Metadata:")
print(metadata)

# Extract image
image = reader.get_image()

print("\nImage Shape:", image.shape)  '''
