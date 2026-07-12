"""
simplify_prompts.py

Prompts used for converting
medical sentences into simple language.
"""


def create_sentence_simplification_prompt(text):
    """
    Creates prompt for sentence simplification.
    """

    prompt = f"""
You are a medical report simplification assistant.

Your task is to convert complex medical language
into simple patient-friendly language.

Rules:
- Preserve the original medical meaning.
- Do not add new medical information.
- Do not provide a diagnosis.
- Explain difficult medical terms.
- Use short and clear sentences.

Medical sentence:

{text}

Simplified sentence:
"""

    return prompt



def create_term_explanation_prompt(term):
    """
    Creates prompt for explaining medical terms.
    """

    prompt = f"""
You are a medical education assistant.

Explain the following medical term
in simple language that a patient can understand.

Rules:
- Keep the explanation short.
- Avoid complex medical words.
- Do not give treatment advice.

Medical term:

{term}

Simple explanation:
"""

    return prompt