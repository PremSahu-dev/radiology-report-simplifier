"""
glossary.py

Main glossary interface.
"""


from glossary.medical_terms import (
    MEDICAL_TERMS
)

from glossary.abbreviations import (
    ABBREVIATIONS
)



class Glossary:


    def __init__(self):

        self.medical_terms = (
            MEDICAL_TERMS
        )

        self.abbreviations = (
            ABBREVIATIONS
        )



    def get_meaning(
        self,
        term
    ):
        """
        Returns explanation of a term.
        """


        key = term.lower()


        if key in self.medical_terms:

            return self.medical_terms[key]


        if term.upper() in self.abbreviations:

            return self.abbreviations[
                term.upper()
            ]


        return term



    def simplify_word(
        self,
        word
    ):
        """
        Used by sentence simplifier.
        """


        meaning = self.get_meaning(
            word
        )


        return meaning



    def contains(
        self,
        term
    ):
        """
        Check if term exists.
        """


        return (
            term.lower()
            in self.medical_terms
            or
            term.upper()
            in self.abbreviations
        )