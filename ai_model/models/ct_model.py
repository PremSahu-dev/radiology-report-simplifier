import torch.nn as nn
from torchvision import models

from models.base_model import BaseModel


class CTModel(BaseModel):
    """
    ResNet50 model for CT scan classification.
    """

    def __init__(self, num_classes=4):
        super().__init__()

        # Load pretrained ResNet50
        self.model = models.resnet50(
            weights=models.ResNet50_Weights.DEFAULT
        )

        # Freeze pretrained layers
        self.freeze_features()

        # Number of input features to the final layer
        in_features = self.model.fc.in_features

        # Replace the final fully connected layer
        self.model.fc = nn.Linear(
            in_features,
            num_classes
        )
