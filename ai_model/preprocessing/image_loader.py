"""
image_loader.py

Universal image loader for DICOM and standard image formats.
"""

import os
import cv2
import pydicom


class ImageLoader:

    @staticmethod
    def load(image_path):
        """
        Loads an image regardless of format.

        Supports:
            .dcm
            .png
            .jpg
            .jpeg

        Returns:
            image (numpy.ndarray)
            metadata (dict)
        """

        extension = os.path.splitext(image_path)[1].lower()

        # -------------------------
        # DICOM
        # -------------------------

        if extension == ".dcm":

            dataset = pydicom.dcmread(image_path)

            image = dataset.pixel_array

            metadata = {

                "modality": dataset.get("Modality", "Unknown"),

                "format": "DICOM"

            }

            return image, metadata

        # -------------------------
        # PNG / JPG / JPEG
        # -------------------------

        elif extension in [".png", ".jpg", ".jpeg"]:

            image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

            metadata = {

                "modality": "MR",

                "format": "IMAGE"

            }

            return image, metadata

        else:

            raise ValueError(
                f"Unsupported image format: {extension}"
            )
