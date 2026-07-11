'''
IMAGE_SIZE = (224, 224)
BATCH_SIZE = 16
NUM_CLASSES = 2
DEVICE = "cuda" or "cpu"
XRAY_MODEL = "DenseNet121"
CT_MODEL = "ResNet50"
MRI_MODEL = "EfficientNetB0"
'''


import torch

# ==========================
# Image Configuration
# ==========================
IMAGE_SIZE = 224

# ==========================
# Training Configuration
# ==========================
BATCH_SIZE = 8
LEARNING_RATE = 1e-4
NUM_EPOCHS = 20

# ==========================
# Device
# ==========================
DEVICE = torch.device(
    "cuda" if torch.cuda.is_available() else "cpu"
)

# ==========================
# Number of Classes
# ==========================
NUM_CLASSES = {
    "MR": 4,
    "CT": 4,
    "CR": 4,
    "DX": 4
}

# ==========================
# Model Configuration
# ==========================
MODEL_NAMES = {
    "MR": "efficientnet_b0",
    "CT": "resnet50",
    "CR": "densenet121",
    "DX": "densenet121"
}



'''
# config.py

# ==========================
# Image Configuration
# ==========================
IMAGE_SIZE = 224

# ==========================
# Training Configuration
# ==========================
BATCH_SIZE = 8
LEARNING_RATE = 1e-4
NUM_EPOCHS = 20

# ==========================
# Device
# ==========================
#DEVICE = "cuda" 
import torch

DEVICE = torch.device(
    "cuda" if torch.cuda.is_available() else "cpu"
)

# ==========================
# Number of Classes
# ==========================
NUM_CLASSES = {
    "MR": 4,
    "CT": 4,
    "CR": 4,   # Computed Radiography (X-ray)
    "DX": 4    # Digital Radiography (X-ray)
}

# ===========================
#Models names
# ===========================
MODEL_NAMES = {
    "MR": "efficientnet_b0",
    "CT": "resnet50",
    "CR": "densenet121",
    "DX": "densenet121"
}
'''
