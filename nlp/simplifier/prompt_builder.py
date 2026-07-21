"""
prompts_builder.py

Builds dynamic prompts for NLP models.
"""


from nlp.prompts.simplify_prompt import (
    SIMPLE_REPORT_SUMMARY_PROMPT,
    SIMPLE_SENTENCE_PROMPT,
    RECOMMENDATION_PROMPT
)



class PromptBuilder:
    """
    Creates prompts for different
    simplification tasks.
    """



    def build_sentence_prompt(
        self,
        sentence
    ):
        """
        Build sentence simplification prompt.
        """


        return SIMPLE_SENTENCE_PROMPT.format(
            text=sentence
        )



    def build_report_prompt(
        self,
        report
    ):
        """
        Build complete report summary prompt.
        """


        return SIMPLE_REPORT_SUMMARY_PROMPT.format(
            report=report
        )



    def build_recommendation_prompt(
        self,
        recommendation
    ):
        """
        Build recommendation prompt.
        """


        return RECOMMENDATION_PROMPT.format(
            recommendation=recommendation
        )



    def build_medical_prompt(
        self,
        data
    ):
        """
        Build complete medical prompt
        from structured report.
        """


        finding = data.get(
            "finding",
            ""
        )


        prediction = data.get(
            "prediction",
            ""
        )


        confidence = data.get(
            "confidence",
            0
        )


        return f"""

You are a medical report simplification assistant.

Convert the following AI generated
medical information into patient friendly language.

Prediction:
{prediction}


Finding:
{finding}


Confidence:
{confidence}%


Rules:

- Use simple words.
- Do not add new medical information.
- Keep the meaning accurate.
- Explain clearly for patients.

"""