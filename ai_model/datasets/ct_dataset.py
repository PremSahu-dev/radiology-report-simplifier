from ai_model.datasets.base_dataset import BaseDataset
from ai_model.preprocessing.dicom_reader import DicomReader


class CTDataset(BaseDataset):

    def __getitem__(self, index):

        dicom_path = self.image_paths[index]

        label = self.labels[index]

        reader = DicomReader(dicom_path)

        reader.load()

        image = reader.get_image()

        metadata = reader.get_metadata()

        processor = self.pipeline.get_preprocessor(
            metadata["modality"]
        )

        image = processor.process(image)

        if self.transform is not None:
           image = self.transform(image)

        return image, label
        
        
        
        
