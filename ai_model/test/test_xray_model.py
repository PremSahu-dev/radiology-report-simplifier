import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

import torch

from config import NUM_CLASSES
from models.xray_model import XRayModel
from datasets.dataset_factory import DatasetFactory
from preprocessing.pipeline import PreprocessingPipeline

# -------------------------------
# X-Ray DICOM file
# -------------------------------

image_paths = [
    "/home/kali/Tproject/radiology-report-simplifier-main/ai_model/preprocessing/imgXR1.dcm"
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
    "CR",
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
# Create model
# -------------------------------

model = XRayModel(
    num_classes=NUM_CLASSES["CR"]
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

print("\nPredicted Class:", prediction.item())
