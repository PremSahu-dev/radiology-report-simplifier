import os
import cv2
import numpy as np
import torch
import torchxrayvision as xrv

from ai_model.preprocessing.dicom_reader import DicomReader
from ai_model.preprocessing.preprocess_xray import XRayPreprocessor
from ai_model.explainability.gradcam import GradCAM
from ai_model.report_generator.report_generator import generate_xray_report


# -------------------------------------------------------
# Device
# -------------------------------------------------------

DEVICE = torch.device(
    "cuda" if torch.cuda.is_available() else "cpu"
)

# -------------------------------------------------------
# Load TorchXRayVision Model
# -------------------------------------------------------

model = xrv.models.get_model("densenet121-res224-all")

model.to(DEVICE)
model.eval()

# -------------------------------------------------------
# Grad-CAM
# -------------------------------------------------------

gradcam = GradCAM(
    model=model,
    target_layer=model.features.denseblock4.denselayer16.conv2
)

# -------------------------------------------------------
# Prediction Function
# -------------------------------------------------------

def predict(image_path):

    # -----------------------------
    # Load DICOM
    # -----------------------------

    reader = DicomReader(image_path)
    reader.load()

    image = reader.get_image()

    # -----------------------------
    # Preprocess
    # -----------------------------

    preprocessor = XRayPreprocessor()

    image = preprocessor.process(image)

    image = torch.from_numpy(image).float()

    image = image.unsqueeze(0).to(DEVICE)

    # -----------------------------
    # Prediction
    # -----------------------------

    with torch.no_grad():
        outputs = model(image)

    outputs = outputs.squeeze().cpu().numpy()

    # -----------------------------
    # Convert predictions
    # -----------------------------

    results = []

    for pathology, score in zip(model.pathologies, outputs):

        results.append({
            "disease": pathology,
            "confidence": round(float(score) * 100, 2)
        })

    results.sort(
        key=lambda x: x["confidence"],
        reverse=True
    )

    # -----------------------------
    # Top prediction index
    # -----------------------------

    best_index = int(np.argmax(outputs))

    # -----------------------------
    # Grad-CAM
    # -----------------------------

    cam = gradcam.generate(
        image,
        class_index=best_index
    )

    cam = cv2.resize(cam, (224, 224))

    heatmap = cv2.applyColorMap(
        np.uint8(cam * 255),
        cv2.COLORMAP_JET
    )

    original = image.squeeze().cpu().numpy()

    original = (original * 255).astype(np.uint8)

    original = cv2.cvtColor(
        original,
        cv2.COLOR_GRAY2BGR
    )

    overlay = cv2.addWeighted(
        original,
        0.5,
        heatmap,
        0.5,
        0
    )

    output_dir = "outputs/gradcam"

    os.makedirs(
        output_dir,
        exist_ok=True
    )

    filename = os.path.basename(image_path)

    filename = os.path.splitext(filename)[0]

    gradcam_path = os.path.join(
        output_dir,
        filename + "_gradcam.jpg"
    )

    cv2.imwrite(
        gradcam_path,
        overlay
    )

    # -----------------------------
    # AI Report
    # -----------------------------

    report = generate_xray_report(results)

    # -----------------------------
    # Return
    # -----------------------------

    return {

        "top_prediction": results[0],

        "all_predictions": results,

        "gradcam_path": gradcam_path,

        "report": report
    }
