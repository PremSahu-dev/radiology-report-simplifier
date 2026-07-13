import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from ai_model.config import NUM_CLASSES
from ai_model.models.mri_model import MRIModel
from ai_model.training.checkpoint import (
    save_checkpoint,
    load_checkpoint
)

# Create model
model = MRIModel(
    num_classes=NUM_CLASSES["MR"]
)

# Save checkpoint
checkpoint_path = "../checkpoints/mri_model_test.pth"

save_checkpoint(
    model,
    checkpoint_path
)

# Load checkpoint
loaded_model = MRIModel(
    num_classes=NUM_CLASSES["MR"]
)

load_checkpoint(
    loaded_model,
    checkpoint_path
)

print("\nCheckpoint test completed successfully.")
