import torch
import torch.nn as nn


class BaseModel(nn.Module):
    """
    Base class for all pretrained medical image models.
    """

    def __init__(self):
        super().__init__()

        self.model = None

    def forward(self, x):
        return self.model(x)

    def freeze_features(self):
        """
        Freeze feature extraction layers.
        """
        for param in self.model.parameters():
            param.requires_grad = False

    def unfreeze_features(self):
        """
        Unfreeze all layers.
        """
        for param in self.model.parameters():
            param.requires_grad = True

    def save_model(self, path):
        """
        Save trained weights.
        """
        torch.save(self.model.state_dict(), path)

    def load_model(self, path, device="cpu"):
        """
        Load trained weights.
        """
        self.model.load_state_dict(
            torch.load(path, map_location=device)
        )
