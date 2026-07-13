"""
dataloader.py

Creates PyTorch DataLoaders for datasets.
"""

from torch.utils.data import DataLoader

from ai_model.config import BATCH_SIZE


def get_dataloader(
    dataset,
    batch_size=BATCH_SIZE,
    shuffle=True,
    num_workers=0
):
    """
    Creates and returns a DataLoader.

    Args:
        dataset (Dataset): PyTorch dataset.
        batch_size (int): Number of samples per batch.
        shuffle (bool): Shuffle data every epoch.
        num_workers (int): Number of worker processes.

    Returns:
        DataLoader
    """

    return DataLoader(
        dataset=dataset,
        batch_size=batch_size,
        shuffle=shuffle,
        num_workers=num_workers
    )
