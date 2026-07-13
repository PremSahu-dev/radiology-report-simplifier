from ai_model.config import NUM_CLASSES

from ai_model.models.mri_model import MRIModel
from ai_model.models.ct_model import CTModel
from ai_model.models.xray_model import XRayModel


class ModelFactory:
    """
    Factory class for creating modality-specific models.
    """

    @staticmethod
    def get_model(modality):
        """
        Returns the appropriate model based on DICOM modality.

        Args:
            modality (str): MR, CT, CR, or DX

        Returns:
            PyTorch model
        """

        modality = modality.upper()

        if modality == "MR":
            return MRIModel(
                num_classes=NUM_CLASSES["MR"]
            )

        elif modality == "CT":
            return CTModel(
                num_classes=NUM_CLASSES["CT"]
            )

        elif modality in ["CR", "DX"]:
            return XRayModel(
                num_classes=NUM_CLASSES[modality]
            )

        else:
            raise ValueError(
                f"Unsupported modality: {modality}"
            )



'''
from ai_model.config import NUM_CLASSES

from ai_model.models.mri_model import MRIModel
from ai_model.models.ct_model import CTModel
from ai_model.models.xray_model import XRayModel


class ModelFactory:

    @staticmethod
    def get_model(modality):

        modality = modality.upper()

        if modality == "MR":
            return MRIModel(
                num_classes=NUM_CLASSES["MR"]
            )

        elif modality == "CT":
            return CTModel(
                num_classes=NUM_CLASSES["CT"]
            )

        elif modality in ["CR", "DX"]:
            return XRayModel(
                num_classes=NUM_CLASSES[modality]
            )

        else:
            raise ValueError(
                f"Unsupported modality: {modality}"
            )
            '''
