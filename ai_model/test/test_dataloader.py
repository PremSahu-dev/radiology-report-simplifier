import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from datasets.dataset_factory import DatasetFactory
from datasets.dataloader import get_dataloader
from preprocessing.pipeline import PreprocessingPipeline


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

print("Batch Size:", loader.batch_size)

for images, labels in loader:

    print("Image Batch Shape:", images.shape)

    print("Label Batch:", labels)

    break
