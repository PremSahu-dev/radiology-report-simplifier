"""
transforms.py

This module contains all PyTorch image transformations
used before sending an image to the CNN model.
"""

'''from torchvision import transforms


def get_default_transform():

    return transforms.Compose([
        transforms.ToPILImage(),
        transforms.ToTensor()
    ])'''
    
from torchvision import transforms


def get_default_transform():

    return transforms.Compose([
        transforms.ToPILImage(),

        # Convert grayscale → RGB
        transforms.Grayscale(num_output_channels=3),

        transforms.ToTensor(),

        # ImageNet normalization
        transforms.Normalize(
            mean=[0.485, 0.456, 0.406],
            std=[0.229, 0.224, 0.225]
        )
    ])
