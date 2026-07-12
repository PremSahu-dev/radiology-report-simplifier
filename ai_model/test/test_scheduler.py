import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from config import NUM_CLASSES
from models.mri_model import MRIModel
from training.optimizer import get_optimizer
from training.scheduler import get_scheduler


model = MRIModel(
    num_classes=NUM_CLASSES["MR"]
)

optimizer = get_optimizer(model)

scheduler = get_scheduler(optimizer)

print("Scheduler:")
print(scheduler)
