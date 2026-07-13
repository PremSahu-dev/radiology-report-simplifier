"""
optimizer.py

This module creates the optimizer
used for training the neural network.
"""

import torch.optim as optim

from ai_model.config import LEARNING_RATE


def get_optimizer(model):
    """
    Returns the Adam optimizer.

    Args:
        model (nn.Module): Neural network model.

    Returns:
        torch.optim.Optimizer
    """

    return optim.Adam(
        model.parameters(),
        lr=LEARNING_RATE
    )
