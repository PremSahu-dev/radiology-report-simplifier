"""
report_pipeline.py

Connects AI + NLP + Report JSON generator.
"""


from ai_model.inference.predict import predict


from nlp.api.interface import process_report
from pdf_generator.generator import generate_pdf


from pdf_generator.report_generator import (
    generate_report_json
)



class ReportPipeline:


    def run(
        self,
        image_path,
        modality,
        patient_id=None,
        file_name=None
    ):

        # -------------------------
        # Step 1
        # AI Prediction
        # -------------------------

        ai_result = predict(
            image_path=image_path,
            modality=modality
        )


        print("AI completed")



        # -------------------------
        # Step 2
        # NLP Processing
        # -------------------------

        nlp_result = process_report(
            ai_result,
            modality
        )


        print("NLP completed")



        # -------------------------
        # Step 3
        # Final JSON Report
        # -------------------------

        final_report = generate_report_json(

            ai_result=ai_result,

            nlp_result=nlp_result,

            modality=modality,

            file_name=file_name,

            patient_id=patient_id

        )
        pdf_result = generate_pdf(

           report_json=final_report,

           output_path="outputs/report.pdf"

        )


        print("Report JSON generated")



        return {

          "report": final_report,

          "pdf": pdf_result

        }