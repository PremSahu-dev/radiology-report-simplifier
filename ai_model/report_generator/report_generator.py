"""
report_generator.py

Generic report generator.
"""

from report_generator.report_templates import REPORTS


def generate_report(modality,
                    prediction,
                    confidence):

    modality = modality.upper()

    if modality not in REPORTS:

        raise ValueError(
            f"Unsupported modality: {modality}"
        )

    if prediction not in REPORTS[modality]:

        raise ValueError(
            f"No report template found for {prediction}"
        )

    report = REPORTS[modality][prediction].copy()

    report["prediction"] = prediction

    report["confidence"] = confidence

    report["disclaimer"] = (
        "This AI-generated report is intended for educational purposes "
        "and should not replace a radiologist's diagnosis."
    )

    return report


def generate_xray_report(predictions):
    """
    Generate a simplified report from X-ray predictions.
    Only the top 3 findings are included.
    """

    top_findings = predictions[:3]

    findings = [
        f"{item['disease']} ({item['confidence']:.2f}%)"
        for item in top_findings
    ]

    return {
        "finding": ", ".join(findings),
        "recommendation":
            "Clinical correlation and radiologist review are recommended.",
        "disclaimer":
            "This AI-generated report is intended for educational purposes and should not replace a radiologist's diagnosis."
    }
