from datasets.base_dataset import BaseDataset

from preprocessing.image_loader import ImageLoader


class MRIDataset(BaseDataset):

    def __getitem__(self, index):

        image_path = self.image_paths[index]

        label = self.labels[index]

        # -------------------------
        # Load image
        # -------------------------

        image, metadata = ImageLoader.load(image_path)

        # -------------------------
        # Preprocess image
        # -------------------------

        processor = self.pipeline.get_preprocessor(
            metadata["modality"]
        )

        image = processor.process(image)

        # -------------------------
        # Apply PyTorch Transform
        # -------------------------

        if self.transform is not None:
            image = self.transform(image)

        return image, label
