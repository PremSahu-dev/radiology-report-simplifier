import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from ai_model.models.model_factory import ModelFactory


modalities = [
    "MR",
    "CT",
    "CR",
    "DX"
]

for modality in modalities:

    model = ModelFactory.get_model(modality)

    print("--------------------------------")

    print("Modality :", modality)

    print("Model :", type(model).__name__)
