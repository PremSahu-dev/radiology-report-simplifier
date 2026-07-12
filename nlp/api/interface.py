"""
interface.py

Public NLP entry point.
"""


from nlp.api.simplify import simplify



def process_report(
    ai_result,
    modality
):

    return simplify(
        ai_result,
        modality
    )