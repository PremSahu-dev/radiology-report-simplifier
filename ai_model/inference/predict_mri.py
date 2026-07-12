from report_generator.report_generator import generate_report
import os
import torch
import torch.nn as nn
from PIL import Image
from torchvision import models, transforms

import cv2
import numpy as np

from explainability.gradcam import GradCAM
from explainability.visualize import overlay_heatmap

# -------------------------------------------------
# Configuration
# -------------------------------------------------

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

MODEL_PATH = os.path.join(
    BASE_DIR,
    "pretrained_models",
    "brain-tumor-detection",
    "multiclass-classification",
    "multi_class_resnet.pth"
)

DEVICE = torch.device(
    "cuda" if torch.cuda.is_available() else "cpu"
)

CLASS_NAMES = [
    "glioma",
    "meningioma",
    "notumor",
    "pituitary"
]

# -------------------------------------------------
# Image Transform
# -------------------------------------------------

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )
])

# -------------------------------------------------
# Load Model
# -------------------------------------------------

model = models.resnet18(weights=None)

num_features = model.fc.in_features
model.fc = nn.Linear(num_features, 4)

state_dict = torch.load(
    MODEL_PATH,
    map_location=DEVICE
)

model.load_state_dict(state_dict)

model.to(DEVICE)
model.eval()
gradcam = GradCAM(
    model=model,
    target_layer=model.layer4
)


# -------------------------------------------------
# Prediction Function
# -------------------------------------------------

def predict(image_path):

    # -------------------------
    # Original Image
    # -------------------------

    original = Image.open(image_path).convert("RGB")

    original_np = np.array(original)

    # -------------------------
    # Model Input
    # -------------------------

    image = transform(original)

    image = image.unsqueeze(0).to(DEVICE)

    # -------------------------
    # Prediction
    # -------------------------

    outputs = model(image)

    probabilities = torch.softmax(outputs, dim=1)

    confidence, predicted = torch.max(
        probabilities,
        dim=1
    )

    predicted_index = predicted.item()

    # -------------------------
    # Grad-CAM
    # -------------------------

    cam = gradcam.generate(
        image,
        predicted_index
    )

    overlay = overlay_heatmap(
        original_np,
        cam
    )

    # -------------------------
    # Save Result
    # -------------------------

    filename = os.path.splitext(
        os.path.basename(image_path)
    )[0]

    output_path = os.path.join(
        BASE_DIR,
        "outputs",
        "gradcam",
        filename + "_gradcam.jpg"
    )

    cv2.imwrite(
        output_path,
        cv2.cvtColor(
            overlay,
            cv2.COLOR_RGB2BGR
        )
    )

    # -------------------------
    # Return
    # -------------------------
    report = generate_report(
        modality="MR",
        prediction=CLASS_NAMES[predicted_index],
        confidence=round(confidence.item() * 100, 2)
    )
    
    

    return {

        "prediction": CLASS_NAMES[predicted_index],

        "confidence": round(
        confidence.item() * 100,
        2
    ),

        "gradcam_path": output_path,

        "report": report
}

if __name__ == "__main__":

    result = predict(
        os.path.join(
            BASE_DIR,
            "dataset",
            "MR",
            "test",
            "glioma",
            "Te-gl_96.jpg"
        )
    )

    print(result)
