# 🧠 AI Model – Radiology Report Simplifier

An AI-powered medical image analysis module developed for the **Radiology Report Simplifier** project.

This module analyzes radiological images, predicts the most likely disease category using deep learning, generates Grad-CAM visual explanations, and produces an AI-generated simplified radiology report.

The project has been designed using a modular architecture so that additional imaging modalities such as **CT** and **X-ray** can be integrated with minimal changes. The current implementation focuses on **MRI brain tumor classification** using a pretrained ResNet18 model.

---

# Features

* MRI brain tumor classification using a pretrained ResNet18 model.
* Automatic image preprocessing.
* Confidence score for every prediction.
* Grad-CAM visualization highlighting important regions used by the model.
* AI-generated simplified radiology report.
* Unified prediction API for future MRI, CT, and X-ray support.
* Modular project structure for easy maintenance and extension.
* Designed for integration with a Django-based web application.

---

# Current Status

| Module                 | Status         |
| ---------------------- | -------------- |
| MRI Classification     | ✅ Completed    |
| Confidence Score       | ✅ Completed    |
| Grad-CAM Visualization | ✅ Completed    |
| Report Generator       | ✅ Completed    |
| Unified AI API         | ✅ Completed    |
| CT Integration         | 🚧 Planned     |
| X-ray Integration      | 🚧 Planned     |
| Django Integration     | 🚧 In Progress |

---

# Technologies Used

* Python 3
* PyTorch
* TorchVision
* Pillow (PIL)
* NumPy
* OpenCV
* Grad-CAM
* Kaggle Dataset
* Git
* Linux (Kali)

---




------------------------------------------------------------------------------------------------------------

# Installation Guide

Follow the steps below to set up the AI module locally.

## 1. Clone the Repository

```bash
git clone <repository-url>
cd radiology-report-simplifier/ai_model
```

## 2. Create a Python Virtual Environment

```bash
python3 -m venv venv
```

Activate the virtual environment:

### Linux / macOS

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

## 3. Install Required Packages

Install the required Python libraries:

```bash
pip install torch torchvision
pip install pillow
pip install numpy
pip install opencv-python
pip install matplotlib
pip install grad-cam
```

Alternatively, if a `requirements.txt` file is available:

```bash
pip install -r requirements.txt
```

## 4. Download the Pretrained Model

Download the pretrained MRI classification model and place it in the following directory:

```
pretrained_models/
└── brain-tumor-detection/
    └── multiclass-classification/
        └── multi_class_resnet.pth
```

## 5. Prepare the Dataset

Organize the MRI dataset using the following directory structure:

```
dataset/
└── MR/
    ├── train/
    ├── test/
    └── val/
```

Each split should contain the following class folders:

* glioma
* meningioma
* notumor
* pituitary

## 6. Verify the Installation

Run the API test to ensure the AI module has been configured correctly:

```bash
python3 -m test.test_api
```

If the installation is successful, the output will include:

* Predicted class
* Confidence score
* Grad-CAM image path
* AI-generated report

The project is now ready for integration with the Django application.




---------------------------------------------------------------------------------------------------------------------------------

# Project Structure

The AI module follows a modular architecture to improve maintainability, scalability, and future expansion to additional medical imaging modalities.

```text
ai_model/
│
├── config.py                     # Global project configuration
│
├── dataset/                      # MRI, CT and X-ray datasets
│   ├── MR/
│   ├── CT/
│   └── XRAY/
│
├── datasets/                     # Dataset classes and data loaders
│
├── preprocessing/                # Image loading and preprocessing pipeline
│
├── models/                       # Deep learning model definitions
│
├── pretrained_models/            # Pretrained model weights
│
├── inference/                    # Prediction API
│
├── explainability/               # Grad-CAM implementation and visualization
│
├── report_generator/             # AI-generated medical report generation
│
├── outputs/                      # Generated Grad-CAM images
│
├── training/                     # Training utilities and scripts
│
├── test/                         # Unit and integration tests
│
├── uploads/                      # Uploaded medical images
│
├── checkpoints/                  # Saved model checkpoints
│
└── utils/                        # Utility functions
```

---

# Folder Description

## dataset/

Stores the medical imaging datasets organized by imaging modality and data split (train, validation, and test).

---

## datasets/

Contains dataset classes responsible for loading images, assigning labels, and preparing batches for the deep learning models.

---

## preprocessing/

Implements the preprocessing pipeline, including image loading, resizing, normalization, and DICOM support.

---

## models/

Contains the neural network architectures used by the project. The current implementation uses a pretrained ResNet18 model for MRI brain tumor classification.

---

## pretrained_models/

Stores pretrained model weights used during inference. These models eliminate the need for lengthy retraining and enable immediate deployment.

---

## inference/

Provides a unified prediction interface for all imaging modalities.

Current implementation:

* MRI ✅
* CT (planned)
* X-ray (planned)

This folder serves as the public API that can be called directly from the Django backend.

---

## explainability/

Implements Grad-CAM to generate visual explanations showing which image regions contributed most to the AI prediction.

---

## report_generator/

Generates simplified AI-assisted radiology reports based on the predicted disease class, confidence score, and imaging modality.

---

## outputs/

Stores generated Grad-CAM images and other future inference outputs.

---

## training/

Contains training scripts, optimizers, schedulers, checkpoints, and other utilities used during model development.

Although the current system relies on pretrained models, this folder allows future retraining using custom datasets.

---

## test/

Contains unit tests and integration tests used to verify the correctness of individual project modules.

---

## uploads/

Acts as the temporary storage location for medical images uploaded through the web application before AI analysis.

---

## checkpoints/

Stores trained model checkpoints created during experimentation and development.

---

## utils/

Reserved for reusable helper functions that may be shared across multiple project modules in future versions.






-------------------------------------------------------------------------------------------------------------------
# Running the AI Module

After completing the installation and setting up the pretrained model and dataset, the AI module can be executed directly from the command line.

## 1. Activate the Virtual Environment

### Linux / macOS

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

---

## 2. Navigate to the AI Module

```bash
cd radiology-report-simplifier/ai_model
```

---

## 3. Run MRI Prediction

```bash
python3 -m inference.predict_mri
```

The system will:

* Load the pretrained MRI classification model.
* Preprocess the input MRI image.
* Predict the tumor class.
* Calculate the confidence score.
* Generate a Grad-CAM visualization.
* Produce an AI-generated simplified radiology report.

---

## Example Output

```python
{
    "prediction": "glioma",
    "confidence": 99.91,
    "gradcam_path": "outputs/gradcam/Te-gl_96_gradcam.jpg",
    "report": {
        "finding": "MRI findings are suggestive of Glioma.",
        "severity": "High",
        "recommendation": "Consult a neurologist or neurosurgeon. Further MRI evaluation and clinical correlation are recommended.",
        "prediction": "glioma",
        "confidence": 99.91,
        "disclaimer": "This AI-generated report is intended for educational purposes and should not replace a radiologist's diagnosis."
    }
}
```

---

## Running the Unified Prediction API

The project exposes a unified prediction interface that can be used by external applications such as the Django backend.





----------------------------------------------------------------------------------------------------------------------------------

# API Reference

The AI module exposes a single public prediction interface that can be used by external applications such as the Django backend.

---

## Prediction Function

```python id="4ycn4o"
from inference.predict import predict
```

Function signature:

```python id="6lcbt9"
predict(image_path, modality)
```

---

## Parameters

| Parameter    | Type  | Description                                                   |
| ------------ | ----- | ------------------------------------------------------------- |
| `image_path` | `str` | Path to the medical image to be analyzed.                     |
| `modality`   | `str` | Imaging modality. Supported values: `"MR"`, `"CT"`, `"XRAY"`. |

---

## Example Usage

```python id="rzylk6"
from inference.predict import predict

result = predict(
    image_path="dataset/MR/test/glioma/Te-gl_96.jpg",
    modality="MR"
)

print(result)
```

---

## Response Format

The function returns a Python dictionary containing the prediction results.

Example:

```python id="r0gwhc"
{
    "prediction": "glioma",
    "confidence": 99.91,
    "gradcam_path": "outputs/gradcam/Te-gl_96_gradcam.jpg",
    "report": {
        "finding": "MRI findings are suggestive of Glioma.",
        "severity": "High",
        "recommendation": "Consult a neurologist or neurosurgeon. Further MRI evaluation and clinical correlation are recommended.",
        "prediction": "glioma",
        "confidence": 99.91,
        "disclaimer": "This AI-generated report is intended for educational purposes and should not replace a radiologist's diagnosis."
    }
}
```

---

## Response Fields

| Field          | Description                                        |
| -------------- | -------------------------------------------------- |
| `prediction`   | Predicted disease class.                           |
| `confidence`   | Prediction confidence expressed as a percentage.   |
| `gradcam_path` | File path of the generated Grad-CAM visualization. |
| `report`       | AI-generated simplified radiology report.          |

---

## Supported Modalities

| Modality | Status            |
| -------- | ----------------- |
| MRI      | ✅ Fully Supported |
| CT       | 🚧 Planned        |
| X-ray    | 🚧 Planned        |

The public API has been intentionally designed to remain unchanged as new imaging modalities are integrated.

---

## Integration Example (Django)

The Django backend can call the AI module as shown below:

```python id="ef86kx"
from inference.predict import predict

result = predict(
    image_path=uploaded_image_path,
    modality="MR"
)

prediction = result["prediction"]
confidence = result["confidence"]
report = result["report"]
gradcam_image = result["gradcam_path"]
```

This interface provides a clean separation between the web application and the AI module, making future maintenance and expansion straightforward.


```python
from inference.predict import predict

result = predict(
    image_path="dataset/MR/test/glioma/Te-gl_96.jpg",
    modality="MR"
)

print(result)
```

Currently supported modalities:

| Modality | Status      |
| -------- | ----------- |
| MRI      | ✅ Supported |
| CT       | 🚧 Planned  |
| X-ray    | 🚧 Planned  |

The API has been designed so that CT and X-ray support can be added in the future without changing the external interface.

---

## Running the API Test

To verify that the complete inference pipeline is working correctly, execute:

```bash
python3 -m test.test_api
```

A successful execution confirms that:

* The pretrained model loads correctly.
* The input image is processed successfully.
* Classification is completed.
* Grad-CAM visualization is generated.
* The AI report is created successfully.










--------------------------------------------------------------------------------------------------------------------------
# Grad-CAM Visualization

To improve the interpretability of the deep learning model, the project uses **Gradient-weighted Class Activation Mapping (Grad-CAM)**.

Grad-CAM highlights the regions of the medical image that contributed most to the model's prediction, allowing users to better understand how the AI reached its decision.

Unlike a standard classification model that only outputs a disease label, Grad-CAM provides a visual explanation by overlaying a heatmap on the original image.

---

## Workflow

The Grad-CAM pipeline performs the following steps:

1. Load the pretrained MRI classification model.
2. Perform a forward pass to obtain the predicted class.
3. Compute gradients for the predicted class.
4. Generate a class activation map from the final convolutional layer.
5. Overlay the heatmap on the original MRI image.
6. Save the visualization to the `outputs/gradcam/` directory.

---

## Output Location

Generated Grad-CAM images are stored in:

```text id="tzlrz0"
outputs/
└── gradcam/
    └── <image_name>_gradcam.jpg
```

Example:

```text id="m5sq9v"
outputs/
└── gradcam/
    └── Te-gl_96_gradcam.jpg
```

---

## Benefits of Grad-CAM

* Improves model interpretability.
* Highlights clinically relevant image regions.
* Assists users in understanding AI predictions.
* Supports explainable AI (XAI) principles.
* Useful for educational demonstrations and project presentations.

---

## Current Implementation

| Feature        | Status        |
| -------------- | ------------- |
| MRI Grad-CAM   | ✅ Implemented |
| CT Grad-CAM    | 🚧 Planned    |
| X-ray Grad-CAM | 🚧 Planned    |

The Grad-CAM implementation has been designed to support additional imaging modalities in future versions with minimal changes to the overall pipeline.





----------------------------------------------------------------------------------------------------------------------

# AI Report Generator

The AI Report Generator converts the model's prediction into a simplified, structured radiology report that is easier to understand.

Instead of returning only a disease label, the system produces a report containing the predicted finding, confidence score, severity assessment, recommendation, and a medical disclaimer.

The report generator has been designed to support multiple imaging modalities through a common interface. While the current implementation focuses on MRI, the same architecture can be extended to CT and X-ray without changing the external API.

---

## Workflow

The report generation process consists of the following steps:

1. Receive the AI prediction from the inference module.
2. Identify the imaging modality.
3. Select the appropriate report template.
4. Populate the template with:

   * Predicted disease
   * Confidence score
   * Severity level
   * Clinical recommendation
5. Return the completed report as a Python dictionary.

---

## Example Report

```python id="ybx2c2"
{
    "finding": "MRI findings are suggestive of Glioma.",
    "severity": "High",
    "recommendation": "Consult a neurologist or neurosurgeon. Further MRI evaluation and clinical correlation are recommended.",
    "prediction": "glioma",
    "confidence": 99.91,
    "disclaimer": "This AI-generated report is intended for educational purposes and should not replace a radiologist's diagnosis."
}
```

---

## Report Fields

| Field            | Description                                                                                   |
| ---------------- | --------------------------------------------------------------------------------------------- |
| `finding`        | Summary of the AI prediction.                                                                 |
| `severity`       | Estimated severity level based on the predicted class.                                        |
| `recommendation` | Suggested next clinical action.                                                               |
| `prediction`     | Predicted disease category.                                                                   |
| `confidence`     | Model confidence score (percentage).                                                          |
| `disclaimer`     | Reminder that the report is AI-generated and does not replace professional medical diagnosis. |

---

## Design Goals

The report generator was developed with the following objectives:

* Produce human-readable summaries of AI predictions.
* Keep the output consistent across imaging modalities.
* Simplify integration with the Django frontend.
* Support future expansion to CT and X-ray reports.
* Maintain a modular template-based architecture for easy customization.

---

## Current Implementation Status

| Feature                | Status        |
| ---------------------- | ------------- |
| MRI Report Generation  | ✅ Implemented |
| CT Report Templates    | 🚧 Planned    |
| X-ray Report Templates | 🚧 Planned    |

The current implementation serves as the foundation for a modality-independent report generation system that can be expanded in future versions.




----------------------------------------------------------------------------------------------------------------------------

# Future Work

The current implementation focuses on MRI brain tumor classification using a pretrained deep learning model. The project has been designed with a modular architecture to support future enhancements without significant changes to the existing codebase.

## Planned Enhancements

### Multi-Modality Support

Extend the AI module to support additional medical imaging modalities:

* CT (Computed Tomography)
* X-ray (CR/DX)

The existing unified prediction API will remain unchanged, allowing these modalities to be integrated seamlessly.

---

### Additional Disease Categories

Expand the system to classify a wider range of medical conditions beyond the current MRI brain tumor classes.

Examples include:

* Stroke
* Intracranial hemorrhage
* Brain metastases
* Lung diseases (X-ray)
* Bone fractures (X-ray)

---

### DICOM-Based Clinical Workflow

Enhance the preprocessing pipeline to fully utilize DICOM metadata, including:

* Patient information
* Study details
* Imaging modality
* Acquisition parameters

This will improve compatibility with real-world clinical datasets.

---

### Improved Explainability

Enhance the explainable AI module by supporting:

* Grad-CAM++
* Score-CAM
* Layer-wise visualization
* Comparative heatmap analysis

These techniques can provide more detailed insights into model predictions.

---

### Advanced Report Generation

Future versions may include:

* Automatic report summarization
* Natural language generation (NLG)
* Clinical terminology simplification
* Multilingual report generation

---

### Web Application Integration

Complete integration with the Django-based frontend to enable:

* Medical image upload
* Real-time AI prediction
* Interactive Grad-CAM visualization
* Automatic report generation
* Report download and sharing

---

### Model Improvements

Future research may explore:

* EfficientNet
* DenseNet
* Vision Transformers (ViT)
* ConvNeXt
* Ensemble learning approaches

to improve classification performance and generalization.

---

### Clinical Validation

Before deployment in real healthcare environments, the system should undergo:

* Large-scale clinical evaluation
* Performance benchmarking
* Validation by certified radiologists
* Regulatory and ethical review

The current implementation is intended for educational and research purposes and is **not** designed for clinical diagnosis or patient care.

----------------------------------------------------------------------------------------------------------------------

# Contributors

This project was developed as part of a college project on Artificial Intelligence and Medical Image Analysis.

## Project

**Radiology Report Simplifier – AI Module**

---

## Team

This project was developed collaboratively by a team of seven students.

| Role                      | Member      |
| ------------------------- | ----------- |
| AI / Deep Learning Module | Anshu Kumar |
| Frontend Development      | Team Member |
| Backend Development       | Team Member |
| Database Design           | Team Member |
| System Integration        | Team Member |
| Testing & Documentation   | Team Member |
| Project Coordination      | Team Member |

*(Replace "Team Member" with the actual names of your teammates.)*

---

## Acknowledgements

The project makes use of publicly available resources, including:

* PyTorch
* TorchVision
* OpenCV
* Pillow (PIL)
* Grad-CAM
* Kaggle datasets
* Open-source pretrained deep learning models

We acknowledge the developers and research community whose tools and datasets made this project possible.

---

## Disclaimer

This project has been developed for **educational and research purposes only**.

The predictions, Grad-CAM visualizations, and AI-generated reports are intended to demonstrate the application of artificial intelligence in medical imaging. They are **not** a substitute for professional medical advice, diagnosis, or treatment.

---

## License

This project is intended for academic use. If distributed publicly, an appropriate open-source license (such as the MIT License) may be added in the future.
