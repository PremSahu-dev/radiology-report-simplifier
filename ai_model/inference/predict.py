"""
predict.py

Unified AI prediction interface.
"""

from ai_model.inference.predict_mri import predict as predict_mri
from ai_model.inference.predict_xray import predict as predict_xray


def predict(image_path, modality):
    """
    Perform AI analysis on a medical image.

    Parameters
    ----------
    image_path : str
        Path to the image.

    modality : str
        MR, CT, XRAY, CR or DX.

    Returns
    -------
    dict

    Example
    -------
    {
        "prediction": "...",
        "confidence": 99.91,
        "gradcam_path": "...",
        "report": {...}
    }
    """

    modality = modality.upper()

    if modality == "MR":
        return predict_mri(image_path)

    if modality == "CT":
        raise NotImplementedError(
            "CT inference is not integrated yet."
        )

    if modality in ("XRAY", "CR", "DX"):
        return predict_xray(image_path)

    raise ValueError(
        f"Unsupported modality: {modality}"
    )
