"""
config.py

Configuration for the NLP Report Simplification module.
"""

# ==========================================
# Hugging Face Model
# ==========================================

MODEL_NAME = "google/flan-t5-base"

# Use this if your system has low RAM:
# MODEL_NAME = "google/flan-t5-small"

# ==========================================
# Generation Parameters
# ==========================================

MAX_INPUT_LENGTH = 512

MAX_OUTPUT_LENGTH = 256

NUM_BEAMS = 4

TEMPERATURE = 0.7

DO_SAMPLE = False

# ==========================================
# Device
# ==========================================

import torch

DEVICE = torch.device(
    "cuda"
    if torch.cuda.is_available()
    else "cpu"
)