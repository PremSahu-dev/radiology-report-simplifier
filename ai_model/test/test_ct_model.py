import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

import torch

from config import NUM_CLASSES
from models.ct_model import CTModel
from datasets.dataset_factory import DatasetFactory
from preprocessing.pipeline import PreprocessingPipeline


# -------------------------------
# CT DICOM file
# -------------------------------

image_paths = [
    "/home/kali/Tproject/radiology-report-simplifier-main/ai_model/preprocessing/imgCT2.dcm"
]

labels = [0]


# -------------------------------
# Create preprocessing pipeline
# -------------------------------

pipeline = PreprocessingPipeline()


# -------------------------------
# Create dataset
# -------------------------------
'''
from preprocessing.dicom_reader import DicomReader

reader = DicomReader(
    "/home/kali/Tproject/radiology-report-simplifier-main/ai_model/preprocessing/imgCT2.dcm"
)

reader.load()

print("Metadata:")
print(reader.get_metadata())

print("\nImage Shape:")
print(reader.get_image().shape)

print("\nNumber of Dimensions:")
print(reader.get_image().ndim)
'''


dataset = DatasetFactory.get_dataset(
    "CT",
    image_paths,
    labels,
    pipeline
)

image, label = dataset[0]

print("Input Tensor Shape:", image.shape)

# Add batch dimension
image = image.unsqueeze(0)

print("Batch Tensor Shape:", image.shape)


# -------------------------------
# Create CT Model
# -------------------------------

model = CTModel(
    num_classes=NUM_CLASSES["CT"]
)

model.eval()


# -------------------------------
# Forward Pass
# -------------------------------

with torch.no_grad():
    output = model(image)

probabilities = torch.softmax(output, dim=1)

prediction = torch.argmax(probabilities, dim=1)

print("\nOutput Shape:", output.shape)

print("\nRaw Output (Logits):")
print(output)

print("\nProbabilities:")
print(probabilities)

#print("\nPredicted Class:")
print("\nPredicted Class:", prediction.item())
#print(prediction.item())
