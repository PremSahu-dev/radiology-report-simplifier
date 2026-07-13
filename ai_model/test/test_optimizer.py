import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from ai_model.models.mri_model import MRIModel
from ai_model.training.optimizer import get_optimizer
from ai_model.config import NUM_CLASSES


model = MRIModel(
    num_classes=NUM_CLASSES["MR"]
)

optimizer = get_optimizer(model)

print("Optimizer:")
print(optimizer)
