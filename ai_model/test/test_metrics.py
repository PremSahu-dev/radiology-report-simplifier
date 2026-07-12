import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from training.metrics import calculate_metrics


# Example labels
y_true = [0, 1, 2, 3]

# Example predictions
y_pred = [0, 1, 1, 3]


metrics = calculate_metrics(
    y_true,
    y_pred
)

print("Metrics:")

for key, value in metrics.items():
    print(f"{key}: {value:.4f}")
