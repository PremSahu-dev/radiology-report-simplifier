"""
dataset_factory.py

Factory for automatically creating datasets for
MRI, CT, and X-ray.
"""

import os

from datasets.mri_dataset import MRIDataset
from datasets.ct_dataset import CTDataset
from datasets.xray_dataset import XRayDataset

from preprocessing.pipeline import PreprocessingPipeline


class DatasetFactory:

    @staticmethod
    def get_dataset(modality, split):
        """
        Creates the appropriate dataset automatically.

        Args:
            modality (str): MR, CT, CR, DX, XRAY
            split (str): train, val, test

        Returns:
            Dataset
        """

        modality = modality.upper()

        # --------------------------------------------------
        # Absolute path to ai_model/
        # --------------------------------------------------

        base_dir = os.path.dirname(
            os.path.dirname(
                os.path.abspath(__file__)
            )
        )

        # --------------------------------------------------
        # Dataset directory
        # --------------------------------------------------

        dataset_root = os.path.join(
            base_dir,
            "dataset",
            modality,
            split
        )

        print(f"Dataset Folder : {dataset_root}")

        if not os.path.exists(dataset_root):
            raise FileNotFoundError(
                f"Dataset folder not found:\n{dataset_root}"
            )

        # --------------------------------------------------
        # Read class folders
        # --------------------------------------------------

        class_names = sorted([
            folder
            for folder in os.listdir(dataset_root)
            if os.path.isdir(
                os.path.join(dataset_root, folder)
            )
        ])

        print(f"Classes Found : {class_names}")

        image_paths = []
        labels = []

        # --------------------------------------------------
        # Scan every class folder
        # --------------------------------------------------

        for label, class_name in enumerate(class_names):

            class_folder = os.path.join(
                dataset_root,
                class_name
            )

            for filename in os.listdir(class_folder):

                if filename.lower().endswith(
                    (
                        ".png",
                        ".jpg",
                        ".jpeg",
                        ".dcm"
                    )
                ):

                    image_paths.append(
                        os.path.join(
                            class_folder,
                            filename
                        )
                    )

                    labels.append(label)

        print(f"Total Images : {len(image_paths)}")

        # --------------------------------------------------
        # Create preprocessing pipeline
        # --------------------------------------------------

        pipeline = PreprocessingPipeline()

        # --------------------------------------------------
        # Create dataset
        # --------------------------------------------------

        if modality == "MR":

            return MRIDataset(
                image_paths=image_paths,
                labels=labels,
                pipeline=pipeline
            )

        elif modality == "CT":

            return CTDataset(
                image_paths=image_paths,
                labels=labels,
                pipeline=pipeline
            )

        elif modality in ["CR", "DX", "XRAY"]:

            return XRayDataset(
                image_paths=image_paths,
                labels=labels,
                pipeline=pipeline
            )

        else:

            raise ValueError(
                f"Unsupported modality: {modality}"
            )
