"""
findings.py

Extracts medical findings from AI output.
"""


class FindingsExtractor:


    def extract(self, ai_result):
        """
        Extract finding information.
        """


        report = ai_result.get(
            "report",
            {}
        )


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


        return {

            "finding": finding,

            "recommendation": recommendation,

            "severity": severity

        }