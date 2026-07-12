"""
simplify.py

Complete NLP pipeline controller.
"""


from nlp.api.inference_adapter import (
    InferenceAdapter
)


from nlp.simplifier.simplifier import (
    simplify_report
)


from nlp.readability.readability_score import (
    ReadabilityScore
)



adapter = InferenceAdapter()

readability = ReadabilityScore()



def simplify(
    ai_result,
    modality
):


    parsed_report = adapter.adapt(
        ai_result,
        modality
    )


    simplified_report = simplify_report(
        parsed_report
    )


    readability_result = readability.calculate(
        simplified_report
    )


    simplified_report["readability"] = (
        readability_result
    )


    return simplified_report