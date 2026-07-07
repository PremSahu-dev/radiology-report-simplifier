import pydicom
import numpy as np


class DicomReader:

    def __init__(self, dicom_path):
        self.dicom_path = dicom_path
        self.dataset = None

    def load(self):
        self.dataset = pydicom.dcmread(self.dicom_path)
        return self.dataset

    def get_image(self):
        return self.dataset.pixel_array

    def get_metadata(self):
        return {
    "patient_id": getattr(self.dataset, "PatientID", "Unknown"),
    "modality": getattr(self.dataset, "Modality", "Unknown"),
    "rows": getattr(self.dataset, "Rows", None),
    "columns": getattr(self.dataset, "Columns", None),
    "study_date": getattr(self.dataset, "StudyDate", "Unknown"),
    "manufacturer": getattr(self.dataset, "Manufacturer", "Unknown"),
    "pixel_spacing": getattr(self.dataset, "PixelSpacing", None),
    "photometric_interpretation": getattr(
        self.dataset,
        "PhotometricInterpretation",
        "Unknown"
    )
}





'''
        return {
            "patient_id": getattr(self.dataset, "PatientID", "Unknown"),
            "modality": getattr(self.dataset, "Modality", "Unknown"),
            "rows": getattr(self.dataset, "Rows", None),
            "columns": getattr(self.dataset, "Columns", None)
        }
'''
