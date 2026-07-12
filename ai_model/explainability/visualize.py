"""
visualize.py

Overlay Grad-CAM heatmap on original image.
"""

import cv2
import numpy as np


def overlay_heatmap(image, cam, alpha=0.4):
    """
    Overlay Grad-CAM heatmap on image.

    Args:
        image : Original RGB image (numpy array)
        cam   : Grad-CAM output (0~1)
        alpha : Heatmap transparency

    Returns:
        Overlay image
    """

    h, w = image.shape[:2]

    cam = cv2.resize(cam, (w, h))

    heatmap = np.uint8(255 * cam)

    heatmap = cv2.applyColorMap(
        heatmap,
        cv2.COLORMAP_JET
    )

    heatmap = cv2.cvtColor(
        heatmap,
        cv2.COLOR_BGR2RGB
    )

    overlay = cv2.addWeighted(
        image,
        1 - alpha,
        heatmap,
        alpha,
        0
    )

    return overlay
