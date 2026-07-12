"""
huggingface_model.py

Wrapper for HuggingFace transformer models
used for medical text simplification.
"""


import torch

from transformers import (
    AutoTokenizer,
    AutoModelForSeq2SeqLM
)



class HuggingFaceModel:
    """
    Handles loading and inference
    of HuggingFace text generation models.
    """



    def __init__(
        self,
        model_name=None
    ):
        """
        Initialize model.

        Parameters
        ----------
        model_name : str
            HuggingFace model name.
        """


        self.model_name = model_name


        self.tokenizer = None

        self.model = None



        if model_name:

            self.load_model(
                model_name
            )



    def load_model(self, model_name):
        """
        Load tokenizer and model.
        """


        self.tokenizer = AutoTokenizer.from_pretrained(
            model_name
        )


        self.model = AutoModelForSeq2SeqLM.from_pretrained(
            model_name
        )



        self.model.eval()



    def generate(
        self,
        text,
        max_length=128
    ):
        """
        Generate simplified text.

        Parameters
        ----------
        text : str
            Input medical sentence


        Returns
        -------
        str
            Simplified sentence
        """


        if self.model is None:

            raise RuntimeError(
                "Model is not loaded"
            )



        inputs = self.tokenizer(
            text,
            return_tensors="pt",
            truncation=True
        )



        with torch.no_grad():

            output_ids = self.model.generate(
                **inputs,
                max_length=max_length,
                num_beams=4
            )



        result = self.tokenizer.decode(
            output_ids[0],
            skip_special_tokens=True
        )



        return result