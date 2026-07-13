import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from ai_model.datasets.dataset_factory import DatasetFactory
from ai_model.preprocessing.pipeline import PreprocessingPipeline

# Replace with your MRI DICOM file
image_paths = [
    "/home/kali/Tproject/radiology-report-simplifier-main/ai_model/preprocessing/imgMR1.dcm"
]

labels = [0]

pipeline = PreprocessingPipeline()

dataset = DatasetFactory.get_dataset(
    "MR",
    image_paths,
    labels,
    pipeline
)

image, label = dataset[0]

print("Image Type:", type(image))
print("Image Shape:", image.shape)
print("Label:", label)
