import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from ai_model.config import NUM_CLASSES

from ai_model.models.mri_model import MRIModel

from ai_model.training.losses import get_loss_function
from ai_model.training.optimizer import get_optimizer
from ai_model.training.scheduler import get_scheduler
from ai_model.training.trainer import Trainer

from ai_model.datasets.dataset_factory import DatasetFactory
from ai_model.datasets.dataloader import get_dataloader

from ai_model.preprocessing.pipeline import PreprocessingPipeline


image_paths = [
    "../preprocessing/imgMR1.dcm"
]

labels = [0]

pipeline = PreprocessingPipeline()

dataset = DatasetFactory.get_dataset(
    "MR",
    image_paths,
    labels,
    pipeline
)

loader = get_dataloader(dataset)

model = MRIModel(
    num_classes=NUM_CLASSES["MR"]
)

criterion = get_loss_function()

optimizer = get_optimizer(model)

scheduler = get_scheduler(optimizer)

trainer = Trainer(
    model=model,
    train_loader=loader,
    optimizer=optimizer,
    criterion=criterion,
    scheduler=scheduler,
    device="cpu"
)

trainer.fit(epochs=3)

'''
loss, labels, predictions = trainer.train_one_epoch()

print("Average Loss:", loss)

print("Labels:", labels)

print("Predictions:", predictions)
'''
