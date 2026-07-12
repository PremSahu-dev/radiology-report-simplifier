"""
report_simplifier.py

Main NLP pipeline for converting
medical reports into patient-friendly reports.
"""


from simplifier.sentence_simplifier import (
    SentenceSimplifier
)

from simplifier.recommendation import (
    RecommendationSimplifier
)

from simplifier.templates_engine import (
    TemplatesEngine
)

from readability.readability_score import (
    ReadabilityScore
)



class ReportSimplifier:
    """
    Complete medical report simplification pipeline.
    """



    def __init__(
        self,
        use_model=False,
        model_name=None
    ):


        self.sentence_simplifier = SentenceSimplifier(
            use_model=use_model,
            model_name=model_name
        )


        self.recommendation_simplifier = (
            RecommendationSimplifier()
        )


        self.template_engine = (
            TemplatesEngine()
        )


        self.readability = (
            ReadabilityScore()
        )



    def simplify(
        self,
        report
    ):
        """
        Simplify complete report.

        Parameters
        ----------
        report : dict


        Returns
        -------
        dict
        """



        finding = report.get(
            "finding",
            ""
        )


        recommendation = report.get(
            "recommendation",
            ""
        )


        severity = report.get(
            "severity",
            ""
        )


        confidence = report.get(
            "confidence",
            None
        )



        # -----------------------------
        # Simplify finding
        # -----------------------------

        simple_finding = (
            self.sentence_simplifier.simplify(
                finding
            )
        )



        # -----------------------------
        # Simplify recommendation
        # -----------------------------

        simple_recommendation = (
            self.recommendation_simplifier.simplify(
                recommendation
            )
        )



        # -----------------------------
        # Create final report
        # -----------------------------

        final_report = (
            self.template_engine.create_report(
                finding=finding,
                explanation=simple_finding,
                severity=severity,
                recommendation=simple_recommendation,
                confidence=confidence
            )
        )



        # -----------------------------
        # Readability
        # -----------------------------

        readability_result = (
            self.readability.calculate(
                final_report
            )
        )



        final_report["readability"] = (
            readability_result
        )



        return final_report