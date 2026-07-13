import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

import torch

from ai_model.config import NUM_CLASSES
from ai_model.models.mri_model import MRIModel
from ai_model.datasets.dataset_factory import DatasetFactory
from ai_model.preprocessing.pipeline import PreprocessingPipeline


# -------------------------------
# MRI DICOM file
# -------------------------------

image_paths = [
    "/home/kali/Tproject/radiology-report-simplifier-main/ai_model/preprocessing/imgMR1.dcm"
]

labels = [0]


# -------------------------------
# Create preprocessing pipeline
# -------------------------------

pipeline = PreprocessingPipeline()


# -------------------------------
# Create dataset
# -------------------------------

dataset = DatasetFactory.get_dataset(
    "MR",
    image_paths,
    labels,
    pipeline
)


# -------------------------------
# Load one image
# -------------------------------

image, label = dataset[0]

print("Input Tensor Shape:", image.shape)


# -------------------------------
# Add batch dimension
# -------------------------------

image = image.unsqueeze(0)

print("Batch Tensor Shape:", image.shape)


# -------------------------------
# Create model
# -------------------------------

model = MRIModel(
    num_classes=NUM_CLASSES["MR"]
)

model.eval()


# -------------------------------
# Forward Pass
# -------------------------------

with torch.no_grad():
    output = model(image)

# Convert logits to probabilities
probabilities = torch.softmax(output, dim=1)

# Get the predicted class
prediction = torch.argmax(probabilities, dim=1)

print("\nOutput Shape:", output.shape)

print("\nRaw Output (Logits):")
print(output)

print("\nProbabilities:")
print(probabilities)

print("\nPredicted Class:")
print(prediction.item())
