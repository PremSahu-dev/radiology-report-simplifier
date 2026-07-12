"""
checkpoint.py

Utility functions for saving and loading model checkpoints.
"""

import os
import torch


def save_checkpoint(model, filepath):
    """
    Saves the model weights.

    Args:
        model (nn.Module): Model to save.
        filepath (str): Destination path.
    """

    os.makedirs(
        os.path.dirname(filepath),
        exist_ok=True
    )

    torch.save(
        model.state_dict(),
        filepath
    )

    print(f"Checkpoint saved to: {filepath}")


def load_checkpoint(model, filepath, device="cpu"):
    """
    Loads model weights.

    Args:
        model (nn.Module): Model instance.
        filepath (str): Path to checkpoint.
        device (str): cpu or cuda.

    Returns:
        nn.Module
    """

    state_dict = torch.load(
        filepath,
        map_location=device
    )

    model.load_state_dict(state_dict)

    print(f"Checkpoint loaded from: {filepath}")

    return model
