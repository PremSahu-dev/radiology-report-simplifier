import sys
import os

# Add ai_model to Python path
sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from ai_model.config import DEVICE

print("Selected Device:", DEVICE)
