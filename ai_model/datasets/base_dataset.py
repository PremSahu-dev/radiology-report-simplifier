from torch.utils.data import Dataset
from preprocessing.transforms import get_default_transform


class BaseDataset(Dataset):

    def __init__(self,
                 image_paths,
                 labels,
                 pipeline,
                 transform=None):
        """
        Base dataset for all medical image modalities.

        Args:
            image_paths (list): List of DICOM file paths.
            labels (list): List of class labels.
            pipeline (PreprocessingPipeline): Preprocessing pipeline instance.
            transform: PyTorch transform (optional)
        """
        super().__init__()

        self.image_paths = image_paths
        self.labels = labels
        self.pipeline = pipeline

        # If no transform is provided, use the default one.
        self.transform = transform or get_default_transform()

    def __len__(self):
        return len(self.image_paths)

    def __getitem__(self, index):
        raise NotImplementedError(
            "Subclasses must implement __getitem__()"
        )
