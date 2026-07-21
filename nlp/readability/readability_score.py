"""
readability_score.py

Calculates readability of
simplified medical reports.
"""


from nlp.readability.sentence_splitter import (
    SentenceSplitter
)



class ReadabilityScore:


    def __init__(self):

        self.splitter = SentenceSplitter()



    def count_words(
        self,
        text
    ):

        return len(
            text.split()
        )



    def count_sentences(
        self,
        text
    ):

        return len(
            self.splitter.split(
                text
            )
        )



    def calculate(
        self,
        report
    ):
        """
        Calculate readability score.

        Uses simplified
        Flesch-like calculation.
        """


        text = (

            report.get(
                "finding",
                ""
            )
            +
            " "
            +
            report.get(
                "explanation",
                ""
            )
            +
            " "
            +
            report.get(
                "recommendation",
                ""
            )

        )



        words = self.count_words(
            text
        )


        sentences = self.count_sentences(
            text
        )



        if words == 0 or sentences == 0:

            return {

                "score":0,

                "level":"Unknown"

            }



        average_words = (
            words / sentences
        )



        # Simple readability scoring

        score = max(
            0,
            min(
                100,
                int(
                    100 -
                    (average_words * 2)
                )
            )
        )



        if score >= 70:

            level = "Easy"



        elif score >= 40:

            level = "Moderate"



        else:

            level = "Difficult"



        return {

            "score": score,

            "level": level

        }