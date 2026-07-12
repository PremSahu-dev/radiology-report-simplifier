"""
metrics.py

Evaluation metrics for model performance.
"""

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)


def calculate_metrics(y_true, y_pred):
    """
    Calculates evaluation metrics.

    Args:
        y_true (list)
        y_pred (list)

    Returns:
        dict
    """

    return {
        "accuracy": accuracy_score(
            y_true,
            y_pred
        ),

        "precision": precision_score(
            y_true,
            y_pred,
            average="weighted",
            zero_division=0
        ),

        "recall": recall_score(
            y_true,
            y_pred,
            average="weighted",
            zero_division=0
        ),

        "f1_score": f1_score(
            y_true,
            y_pred,
            average="weighted",
            zero_division=0
        )
    }
