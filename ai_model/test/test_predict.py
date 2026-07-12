import os

from inference.predict import predict

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

image_path = os.path.join(
    BASE_DIR,
    "dataset",
    "MR",
    "test",
    "glioma",
    "Te-gl_96.jpg"
)

result = predict(
    image_path=image_path,
    modality="MR"
)

print(result)
