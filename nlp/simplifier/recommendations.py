"""
recommendation.py

Simplifies medical recommendations
into patient-friendly instructions.
"""


from nlp.glossary.glossary import Glossary



class RecommendationSimplifier:
    """
    Converts medical recommendations
    into simpler language.
    """



    def __init__(self):

        self.glossary = Glossary()



    def simplify(
        self,
        recommendation
    ):
        """
        Simplify recommendation text.

        Parameters
        ----------
        recommendation : str

        Returns
        -------
        str
        """

        if not recommendation:

            return ""



        simplified = recommendation



        replacements = {

            "clinical correlation":
                "doctor's evaluation",

            "neurologist":
                "brain specialist",

            "neurosurgeon":
                "brain surgery specialist",

            "radiologist":
                "medical imaging specialist",

            "further evaluation":
                "additional checking",

            "follow-up imaging":
                "another scan later if required"

        }



        for old, new in replacements.items():

            simplified = simplified.replace(
                old,
                new
            )



        return simplified