"""
postprocess.py

Cleans and formats generated NLP output.
"""


import re



class PostProcessor:
    """
    Text cleaning utility after
    AI text generation.
    """



    def clean(self, text):
        """
        Clean generated text.

        Parameters
        ----------
        text : str
            Generated output


        Returns
        -------
        str
            Clean text
        """


        if not text:

            return ""



        # Remove extra spaces

        text = re.sub(
            r"\s+",
            " ",
            text
        )



        # Remove spaces before punctuation

        text = re.sub(
            r"\s([,.!?])",
            r"\1",
            text
        )



        # Remove repeated punctuation

        text = re.sub(
            r"([.!?]){2,}",
            r"\1",
            text
        )



        return text.strip()



    def format_paragraph(
        self,
        sentences
    ):
        """
        Combine sentences into
        readable paragraph.
        """


        if not sentences:

            return ""



        paragraph = " ".join(
            sentence.strip()
            for sentence in sentences
        )


        return self.clean(
            paragraph
        )