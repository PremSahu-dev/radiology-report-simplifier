"""
generator.py

Public PDF generator API.
"""


from pdf_generator.report_formatter import (
    format_report
)


from pdf_generator.pdf_builder import (
    build_pdf
)



def generate_pdf(
        report_json,
        output_path
):
    """
    Generates PDF and returns
    PDF path with report JSON.
    """


    formatted_report = format_report(
        report_json
    )


    pdf_path = build_pdf(

        formatted_report,

        output_path

    )


    return {

        "status": "success",

        "pdf_path": pdf_path,

        "report": report_json

    }