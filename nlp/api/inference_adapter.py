"""
inference_adapter.py

Connects AI module output
with NLP parser.
"""


from nlp.report_parse.parser import ReportParser



class InferenceAdapter:


    def __init__(self):

        self.parser = ReportParser()



    def adapt(
        self,
        ai_result,
        modality
    ):

        return self.parser.parse(
            ai_result,
            modality
        )