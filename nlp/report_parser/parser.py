"""
parser.py

Main report parser.
"""


from report_parse.findings import (
    FindingsExtractor
)

from report_parse.metadata import (
    MetadataExtractor
)



class ReportParser:


    def __init__(self):

        self.findings = (
            FindingsExtractor()
        )

        self.metadata = (
            MetadataExtractor()
        )



    def parse(
        self,
        ai_result,
        modality
    ):
        """
        Convert AI output into
        common NLP input format.
        """


        metadata = self.metadata.extract(
            ai_result,
            modality
        )


        findings = self.findings.extract(
            ai_result
        )


        parsed_report = {


            "modality":
                metadata["modality"],


            "prediction":
                metadata["prediction"],


            "confidence":
                metadata["confidence"],


            "finding":
                findings["finding"],


            "severity":
                findings["severity"],


            "recommendation":
                findings["recommendation"]

        }


        return parsed_report