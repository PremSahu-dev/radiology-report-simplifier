"""
image_handler.py

Handles images in PDF.
"""


from reportlab.platypus import Image



def load_image(
        image_path
):


    try:

        img = Image(
            image_path,
            width=250,
            height=250
        )

        return img


    except Exception:

        return None