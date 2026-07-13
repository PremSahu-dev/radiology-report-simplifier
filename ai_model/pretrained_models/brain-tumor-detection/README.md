---
license: mit
metrics:
- accuracy
- precision
- recall
- f1
base_model:
- microsoft/resnet-18
pipeline_tag: image-classification
tags:
- deep-learning
- computer-vision
- medical-imaging
---
# Model Card: Brain Tumor Multi-Class Classification

## Model Details

### Model Description
A fine-tuned ResNet18 convolutional neural network for classifying brain MRI scans into four categories of brain tumors. The model uses transfer learning with ImageNet pre-trained weights and has been adapted for medical image classification.

- **Developed by:** Thisen Ekanayake
- **Model type:** Convolutional Neural Network (ResNet18)
- **Language(s):** Python (PyTorch)
- **License:** MIT License
- **Demo:** https://brainet.thisenekanayake.me
- **Parent Model:** ResNet18 (pretrained on ImageNet)
- **Model Variants:** This model card focuses on the **multi-class classification model** (4 classes: glioma, meningioma, no tumor, pituitary). A **binary classification model** (tumor vs. no tumor) is also available in the GitHub repository with complete training and evaluation scripts.

### Model Architecture
- **Base Architecture:** ResNet18
- **Input:** RGB images resized to 224x224 pixels
- **Output:** 4-class classification (glioma, meningioma, notumor, pituitary)
- **Modifications:** 
  - Final fully connected layer replaced with 4-class output
  - Early layers frozen during training
  - Only layer4 and final FC layer fine-tuned
- **Parameters:** ~11M total parameters

## Intended Uses

### Primary Use Case
This model is designed for **research and educational purposes only** to demonstrate deep learning applications in medical image analysis. It can be used to:
- Study transfer learning techniques in medical imaging
- Explore brain tumor classification methodologies
- Educational demonstrations of CNN architectures
- Research prototyping and benchmarking

### Out-of-Scope Uses
- **NOT for clinical diagnosis or treatment decisions**
- **NOT for patient care or medical decision-making**
- **NOT a replacement for professional medical evaluation**
- **NOT validated for deployment in healthcare settings**
- Should not be used without expert medical supervision

## Training Data

### Dataset Information
- **Source:** Brain Tumor Segmentation(BraTS2020)
- **Dataset Link:** https://www.kaggle.com/datasets/awsaf49/brats2020-training-data
- **Classes:** 
  1. Glioma
  2. Meningioma
  3. No Tumor
  4. Pituitary Tumor

### Dataset Statistics
- **Training samples:** 5712
- **Testing samples:** 1311
- **Class Distribution (Training):**
  - Imbalanced dataset with varying samples per class
  - Weighted sampling used to address class imbalance
  - Class weights applied during training

### Data Preprocessing
- **Image Resizing:** 224x224 pixels
- **Normalization:** ImageNet statistics (mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
- **Training Augmentations:**
  - Random horizontal flip (p=0.5)
  - Random rotation (±10 degrees)
  - Color jitter (brightness=0.2, contrast=0.2)
- **Test Preprocessing:** Resize and normalize only (no augmentation)

### Known Dataset Limitations
- Limited diversity in imaging protocols and scanner types
- Potential demographic biases in patient populations
- Images may not represent all tumor subtypes or presentations
- Dataset size may limit generalization to rare cases
- Quality and annotation consistency may vary

## Model Performance

### Overall Metrics (Test Set)
Evaluated on **1,311 test samples** with **1,298 correct predictions** (13 errors):

| Metric | Weighted Avg | Macro Avg |
|--------|--------------|-----------|
| **Accuracy** | **99.01%** | - |
| **Precision** | **99.03%** | 98.96% |
| **Recall** | **99.01%** | 98.92% |
| **F1 Score** | **99.01%** | 98.92% |

### Per-Class Performance

| Class | Precision | Recall | F1 Score | Support |
|-------|-----------|--------|----------|---------|
| **Glioma** | 99.66% | 96.33% | 97.97% | 300 |
| **Meningioma** | 96.53% | 100.00% | 98.23% | 306 |
| **No Tumor** | 100.00% | 100.00% | 100.00% | 405 |
| **Pituitary** | 99.67% | 99.33% | 99.50% | 300 |

#### Detailed Analysis by Class

**Glioma:**
- Correctly classified: 289/300 (96.33%)
- Misclassified as Meningioma: 10 cases
- Misclassified as Pituitary: 1 case
- High precision (99.66%) indicates few false positives

**Meningioma:**
- Correctly classified: 306/306 (100% recall)
- Perfect recall with no false negatives
- Precision of 96.53% due to 11 false positives from other classes

**No Tumor:**
- Perfect classification (100% precision, recall, and F1)
- 405/405 correctly identified
- No confusion with tumor classes

**Pituitary:**
- Correctly classified: 298/300 (99.33%)
- Misclassified as Glioma: 1 case
- Misclassified as Meningioma: 1 case
- Near-perfect performance across all metrics

### Confusion Analysis
- **Total Errors:** 13 out of 1,311 samples (0.99% error rate)
- **Most Common Error:** Glioma misclassified as Meningioma (10 cases)
- **Best Performance:** No Tumor class (perfect classification)
- **Clinical Significance:** The model never confuses tumor cases with "No Tumor", which is critical for medical screening applications

## Training Procedure

### Training Configuration
- **Framework:** PyTorch
- **Optimizer:** Adam
- **Learning Rate:** 1e-4
- **Batch Size:** 16
- **Loss Function:** CrossEntropyLoss with class weights
- **Device:** CUDA (GPU) Nvidia GeForce RTX 4060 8GB 
- **Training Strategy:** Transfer learning with partial fine-tuning

### Training Details
1. **Layer Freezing:** All layers frozen except layer4 and final FC layer
2. **Class Imbalance Handling:** 
   - Weighted random sampling during training
   - Class-weighted loss function
3. **Validation:** Evaluated on test set after each epoch
4. **Early Stopping:** Not implemented (trained for full 10 epochs)

### Computational Requirements
- **Training Time:** Hardware dependent
- **GPU Memory:** Suitable for single GPU training
- **Inference Time:** Fast inference suitable for real-time applications

## Limitations and Biases

### Technical Limitations
1. **Input Constraints:** 
   - Requires specific image dimensions (224x224)
   - Expects RGB format with ImageNet normalization
   - May not handle varying image qualities well

2. **Performance Limitations:**
   - Trained on limited dataset size
   - May not generalize to images from different scanners or protocols
   - Performance on edge cases and rare tumor types unknown

3. **Architectural Limitations:**
   - ResNet18 is relatively shallow; deeper models might capture more complex patterns
   - Single-view classification (doesn't utilize 3D MRI volumes)
   - No attention mechanisms or interpretability features

### Potential Biases
1. **Dataset Bias:**
   - Training data may not represent global population diversity
   - Potential geographical, demographic, or institutional biases
   - Scanner and imaging protocol biases

2. **Class Imbalance:**
   - Despite weighted sampling, model may still favor majority classes
   - Rare tumor presentations underrepresented

3. **Annotation Bias:**
   - Dependent on original dataset annotation quality
   - May inherit labeling errors or inconsistencies

### Medical and Ethical Considerations
1. **NOT Clinically Validated:**
   - No regulatory approval (FDA, CE, etc.)
   - Not tested in real clinical workflows
   - Performance on real-world clinical data unknown

2. **Risk of Misuse:**
   - Should never replace professional medical judgment
   - False positives/negatives could lead to inappropriate actions if misused
   - Requires proper medical context for interpretation

3. **Privacy Considerations:**
   - Ensure patient data privacy when using model
   - Comply with HIPAA, GDPR, and local regulations
   - Anonymize any input images appropriately

## Recommendations

### For Researchers and Developers
- Use as baseline or comparison model for brain tumor classification research
- Experiment with different architectures, hyperparameters, or training strategies
- Combine with other models or modalities for improved performance
- Conduct thorough validation on your specific use case

### For Educators
- Excellent demonstration of transfer learning in medical imaging
- Shows importance of handling class imbalance
- Good example of CNN fine-tuning strategies
- Can be used to teach medical AI ethics and limitations

### Best Practices
1. Always validate model predictions with ground truth when available
2. Use ensemble methods or multiple models for critical applications
3. Implement uncertainty quantification to identify low-confidence predictions
4. Continuously monitor model performance on new data
5. Maintain human oversight for all predictions

## How to Use

### Loading the Model
```python
import torch
import torch.nn as nn
from torchvision import models

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Load model architecture
model = models.resnet18(pretrained=False)
num_ftrs = model.fc.in_features
model.fc = nn.Linear(num_ftrs, 4)
model = model.to(device)

# Load trained weights
model.load_state_dict(torch.load("multi_class_resnet.pth"))
model.eval()
```

### Image Preprocessing
```python
from torchvision import transforms

test_transforms = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])
```

### Making Predictions
```python
with torch.no_grad():
    image = test_transforms(pil_image).unsqueeze(0).to(device)
    output = model(image)
    _, prediction = torch.max(output, 1)
    
class_names = ['glioma', 'meningioma', 'notumor', 'pituitary']
predicted_class = class_names[prediction.item()]
```

## Citation

If you use this model in your research, please cite:

```bibtex
@misc{brain_tumor_classifier_2025,
  title={BRAINet - Brain Tumor Multi-Class Classification using ResNet18},
  author={Thisen Ekanayake},
  year={2025},
  url={https://brainet.thisenekanayake.me},
  note={Educational and research purposes only}
}
```

### Dataset Citation
```bibtex
@misc{brats20_dataset,
  author={Awsaf},
  title={Brain Tumor Segmentation(BraTS2020)},
  year={2020},
  url={https://www.kaggle.com/datasets/awsaf49/brats2020-training-data}
}
```

## Contact and Support

- **Demo Application:** https://brainet.thisenekanayake.me
- **GitHub Repository:** https://github.com/Thisen-Ekanayake/BRAINet
- **Binary Classification Model:** Available in the repository with complete training and evaluation scripts
- **Issues:** Submit issues via the GitHub repository
- **Contributions:** Welcome via pull requests to the [BRAINet GitHub repository](https://github.com/Thisen-Ekanayake/BRAINet.git)

## Model Card Version

- **Version:** 1.0
- **Date:** February 2026
- **Last Updated:** February 2026

## Glossary

- **Glioma:** A type of tumor that occurs in the brain and spinal cord
- **Meningioma:** A tumor that arises from the meninges (membranes surrounding the brain and spinal cord)
- **Pituitary Tumor:** A growth in the pituitary gland
- **Transfer Learning:** Using a pre-trained model and adapting it for a new task
- **Fine-tuning:** Training select layers of a pre-trained model on new data
- **Class Imbalance:** When training data has unequal numbers of samples per class

---

## ⚠️ CRITICAL DISCLAIMER

**THIS MODEL IS FOR RESEARCH AND EDUCATIONAL PURPOSES ONLY**

This model has NOT been validated for clinical use and should NEVER be used for:
- Medical diagnosis
- Treatment planning
- Patient care decisions
- Clinical decision support

Always consult qualified healthcare professionals for medical advice, diagnosis, and treatment. The developers assume no liability for misuse of this model in clinical or medical settings.

---

*This model card follows the framework proposed by Mitchell et al. (2019) and adapted for medical AI applications.*