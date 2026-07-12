"""
scheduler.py

This module creates the learning rate scheduler.
"""

from torch.optim.lr_scheduler import StepLR


def get_scheduler(optimizer):
    """
    Returns the learning rate scheduler.

    Args:
        optimizer: Optimizer instance.

    Returns:
        StepLR scheduler.
    """

    return StepLR(
        optimizer,
        step_size=5,
        gamma=0.5
    )
