from inference.predict import predict
import os

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

print("=" * 60)
print("MRI TEST")
print("=" * 60)

mri_image = os.path.join(
    BASE_DIR,
    "dataset",
    "MR",
    "test",
    "glioma",
    "Te-gl_96.jpg"
)

mri_result = predict(
    image_path=mri_image,
    modality="MR"
)

print(mri_result)

print("\n" + "=" * 60)
print("X-RAY TEST")
print("=" * 60)

xray_image = os.path.join(
    BASE_DIR,
    "dataset",
    "XRAY",
    "test",
    "000001.dcm"      # Change this if your filename is different
)

xray_result = predict(
    image_path=xray_image,
    modality="CR"
)

print(xray_result)
