"""
train.py

Main training script.
"""

import torch
from torch.utils.data import DataLoader

from config import *

from datasets.dataset_factory import DatasetFactory
from models.model_factory import ModelFactory

from training.losses import get_loss_function
from training.optimizer import get_optimizer
from training.scheduler import get_scheduler
from training.trainer import Trainer


def main():
    """
    Main training function.
    """

    # -------------------------
    # Select Modality
    # -------------------------

    modality = "MR"

    # -------------------------
    # Device
    # -------------------------

    device = torch.device(DEVICE)

    print("=" * 50)
    print("Radiology Report Simplifier - Training")
    print("=" * 50)
    print(f"Modality     : {modality}")
    print(f"Device       : {device}")
    print()

    # -------------------------
    # Create Dataset
    # -------------------------

    dataset = DatasetFactory.get_dataset(
        modality=modality,
        split="train"
    )

    print(f"Dataset Size : {len(dataset)}")

    # -------------------------
    # Create DataLoader
    # -------------------------

    train_loader = DataLoader(
        dataset,
        batch_size=BATCH_SIZE,
        shuffle=True
    )

    print(f"Batch Size   : {BATCH_SIZE}")
    print()

    # -------------------------
    # Create Model
    # -------------------------

    model = ModelFactory.create_model(modality)

    print(f"Model        : {model.__class__.__name__}")
    print()

    # -------------------------
    # Create Loss Function
    # -------------------------

    criterion = get_loss_function()

    print(f"Loss Function: {criterion}")

    # -------------------------
    # Create Optimizer
    # -------------------------

    optimizer = get_optimizer(model)

    print(f"Optimizer    : {optimizer.__class__.__name__}")

    # -------------------------
    # Create Scheduler
    # -------------------------

    scheduler = get_scheduler(optimizer)

    print(f"Scheduler    : {scheduler.__class__.__name__}")
    print()

    # -------------------------
    # Create Trainer
    # -------------------------

    trainer = Trainer(
        model=model,
        train_loader=train_loader,
        optimizer=optimizer,
        criterion=criterion,
        scheduler=scheduler,
        device=device
    )

    print("Trainer      : Ready")
    print()

    # -------------------------
    # Start Training
    # -------------------------

    print("Starting Training...\n")

    trainer.fit(epochs=NUM_EPOCHS)

    print("\nTraining Completed Successfully!")


if __name__ == "__main__":
    main()
