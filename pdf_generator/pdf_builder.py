"""
pdf_builder.py

Creates PDF document.
"""


from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)


from reportlab.lib.styles import (
    getSampleStyleSheet
)


from pdf_generator.config import (
    DISCLAIMER
)


from pdf_generator.image_handler import (
    load_image
)



def build_pdf(
        report,
        output_path
):


    document = SimpleDocTemplate(
        output_path
    )


    styles = getSampleStyleSheet()


    content = []



    def add_section(
            title,
            value
    ):

        content.append(

            Paragraph(
                f"<b>{title}</b>",
                styles["Heading3"]
            )

        )


        content.append(

            Paragraph(
                str(value),
                styles["BodyText"]
            )

        )


        content.append(
            Spacer(1,12)
        )



    # Title

    content.append(

        Paragraph(
            "Radiology AI Report",
            styles["Title"]
        )

    )


    content.append(
        Spacer(1,20)
    )



    add_section(
        "Patient Information",
        report["patient"]
    )



    add_section(
        "Scan Information",
        report["scan"]
    )



    add_section(
        "AI Prediction",
        report["ai"]
    )



    add_section(
        "Medical Finding",
        report["medical"]
    )



    add_section(
        "Patient Friendly Explanation",
        report["simple"]
    )



    add_section(
        "Readability Score",
        report["readability"]
    )



    gradcam = (

        report["ai"]
        .get(
            "gradcam_path"
        )

    )



    if gradcam:


        image = load_image(
            gradcam
        )


        if image:

            content.append(
                Paragraph(
                    "AI Visualization",
                    styles["Heading3"]
                )
            )


            content.append(
                image
            )



    content.append(

        Paragraph(
            DISCLAIMER,
            styles["Italic"]
        )

    )



    document.build(
        content
    )


    return output_path