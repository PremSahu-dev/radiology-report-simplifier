"""
sentence_splitter.py

Splits medical report text
into individual sentences.
"""


import re



class SentenceSplitter:
    """
    Sentence splitting utility.
    """



    def split(
        self,
        text
    ):
        """
        Split paragraph into sentences.

        Parameters
        ----------
        text : str


        Returns
        -------
        list
        """



        if not text:

            return []



        sentences = re.split(
            r'(?<=[.!?])\s+',
            text.strip()
        )


        return [
            sentence.strip()
            for sentence in sentences
            if sentence.strip()
        ]