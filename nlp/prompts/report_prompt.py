"""
report_prompts.py

Prompts for generating simplified
patient-friendly radiology reports.
"""


def create_report_simplification_prompt(
        finding,
        severity,
        recommendation,
        prediction,
        confidence
):
    """
    Creates complete report simplification prompt.
    """

    prompt = f"""
You are an AI medical report simplification assistant.

Convert the following AI-generated radiology
information into a patient-friendly explanation.

Medical Information:

Prediction:
{prediction}

Confidence:
{confidence}%

Finding:
{finding}

Severity:
{severity}

Recommendation:
{recommendation}


Instructions:

1. Explain the finding in simple language.
2. Explain medical terms if needed.
3. Keep the original meaning unchanged.
4. Do not create additional medical facts.
5. Do not replace a doctor's diagnosis.
6. Use a calm and understandable tone.


Generate output in this format:

Explanation:
- 

What this means:
-

Recommended next step:
-

"""

    return prompt



def create_summary_prompt(report):
    """
    Creates short summary prompt.
    """

    prompt = f"""
Summarize this medical report
for a patient.

Rules:
- Use simple language.
- Keep it within 2-3 sentences.
- Do not add new information.

Report:

{report}


Summary:
"""

    return prompt