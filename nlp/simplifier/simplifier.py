"""
simplifier.py

Main entry point for NLP report simplification.
"""


from simplifier.report_simplifier import (
    ReportSimplifier
)



# Default NLP engine

_report_simplifier = ReportSimplifier()



def simplify_report(
    report
):
    """
    Simplify medical AI report.

    Parameters
    ----------
    report : dict
        AI generated report


    Returns
    -------
    dict
        Patient friendly report
    """



    return _report_simplifier.simplify(
        report
    )