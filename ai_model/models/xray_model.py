import torch.nn as nn
from torchvision import models

from ai_model.models.base_model import BaseModel


class XRayModel(BaseModel):
    
   # DenseNet121 model for X-ray classification.

    def __init__(self, num_classes=4):
        super().__init__()

        # Load pretrained DenseNet121
        self.model = models.densenet121(
            weights=models.DenseNet121_Weights.DEFAULT
        )

        # Freeze pretrained layers
        self.freeze_features()

        # Number of input features to classifier
        in_features = self.model.classifier.in_features

        # Replace classifier
        self.model.classifier = nn.Linear(
            in_features,
            num_classes
        )
