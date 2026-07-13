import torch.nn as nn
from torchvision import models

from ai_model.models.base_model import BaseModel


class MRIModel(BaseModel):
    """
    EfficientNet-B0 model for MRI classification.
    """

    def __init__(self, num_classes=4):
        super().__init__()

        # Load pretrained EfficientNet-B0
        self.model = models.efficientnet_b0(
            weights=models.EfficientNet_B0_Weights.DEFAULT
        )

        # Freeze pretrained layers
        self.freeze_features()

        # Replace classifier
        in_features = self.model.classifier[1].in_features

        self.model.classifier[1] = nn.Linear(
            in_features,
            num_classes
        )
