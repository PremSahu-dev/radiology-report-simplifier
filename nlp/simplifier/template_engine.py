"""
templates_engine.py

Creates structured report templates
for final patient reports.
"""



class TemplatesEngine:
    """
    Generates standard report format.
    """



    def create_report(
        self,
        finding="",
        explanation="",
        severity="",
        recommendation="",
        confidence=None,
        disclaimer=None
    ):
        """
        Create structured medical report.

        Returns
        -------
        dict
        """



        report = {


            "title":
                "AI Generated Medical Report",



            "finding":
                finding,



            "explanation":
                explanation,



            "severity":
                severity,



            "recommendation":
                recommendation,



            "confidence":
                confidence,



            "disclaimer":
                disclaimer

                or

                (
                "This report is generated "
                "using artificial intelligence "
                "and should not replace "
                "professional medical advice."
                )

        }



        return report



    def create_summary(
        self,
        finding,
        recommendation
    ):
        """
        Creates short patient summary.
        """



        return {

            "summary":
                (
                f"{finding} "
                f"{recommendation}"
                )

        }