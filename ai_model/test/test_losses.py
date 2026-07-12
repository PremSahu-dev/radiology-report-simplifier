import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from training.losses import get_loss_function


loss_function = get_loss_function()

print("Loss Function:")
print(loss_function)
