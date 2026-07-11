from datasets.xray_dataset import XRayDataset
from datasets.ct_dataset import CTDataset
from datasets.mri_dataset import MRIDataset


class DatasetFactory:

    @staticmethod
    def get_dataset(modality, image_paths, labels, pipeline):

        modality = modality.upper()

        if modality in ["CR", "DX"]:
            return XRayDataset(
                image_paths,
                labels,
                pipeline
            )

        elif modality == "CT":
            return CTDataset(
                image_paths,
                labels,
                pipeline
            )

        elif modality == "MR":
            return MRIDataset(
                image_paths,
                labels,
                pipeline
            )

        else:
            raise ValueError(
                f"Unsupported modality: {modality}"
            )
