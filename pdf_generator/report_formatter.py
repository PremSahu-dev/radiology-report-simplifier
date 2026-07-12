"""
report_formatter.py

Formats report data for PDF.
"""


def format_report(report):

    return {


        "patient":

        report.get(
            "patient",
            {}
        ),



        "scan":

        report.get(
            "scan",
            {}
        ),



        "ai":

        report.get(
            "ai_result",
            {}
        ),



        "medical":

        report.get(
            "medical_report",
            {}
        ),



        "simple":

        report.get(
            "simplified_report",
            {}
        ),



        "readability":

        report.get(
            "readability",
            {}
        ),



        "metadata":

        report.get(
            "metadata",
            {}
        )

    }