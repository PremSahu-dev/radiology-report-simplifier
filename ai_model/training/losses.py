"""
losses.py

This module contains the loss functions used
during model training.
"""

import torch.nn as nn


def get_loss_function():
    """
    Returns the loss function for multi-class classification.

    Returns:
        nn.Module
    """

    return nn.CrossEntropyLoss()
