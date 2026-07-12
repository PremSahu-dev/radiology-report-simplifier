"""
gradcam.py

Grad-CAM implementation for ResNet18.
"""

import torch
import torch.nn.functional as F


class GradCAM:

    def __init__(self, model, target_layer):

        self.model = model
        self.target_layer = target_layer

        self.activations = None
        self.gradients = None

        self.forward_handle = target_layer.register_forward_hook(
            self.forward_hook
        )

        self.backward_handle = target_layer.register_full_backward_hook(
            self.backward_hook
        )

    def forward_hook(self, module, input, output):
        self.activations = output

    def backward_hook(self, module, grad_input, grad_output):
        self.gradients = grad_output[0]

    def generate(self, image_tensor, class_index=None):

        self.model.eval()

        output = self.model(image_tensor)

        if class_index is None:
            class_index = torch.argmax(output).item()

        self.model.zero_grad()

        score = output[0, class_index]

        score.backward()

        gradients = self.gradients
        activations = self.activations

        weights = gradients.mean(dim=(2, 3), keepdim=True)

        cam = (weights * activations).sum(dim=1)

        cam = F.relu(cam)

        cam = cam.squeeze()

        cam -= cam.min()

        if cam.max() > 0:
            cam /= cam.max()

        return cam.detach().cpu().numpy()

    def remove_hooks(self):

        self.forward_handle.remove()
        self.backward_handle.remove()
