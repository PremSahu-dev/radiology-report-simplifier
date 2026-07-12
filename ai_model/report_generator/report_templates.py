"""
report_templates.py

Templates for AI-generated simplified reports.
"""

REPORTS = {

    "MR": {

        "glioma": {

            "finding":
                "MRI findings are suggestive of Glioma.",

            "severity":
                "High",

            "recommendation":
                "Consult a neurologist or neurosurgeon. Further MRI evaluation and clinical correlation are recommended."

        },

        "meningioma": {

            "finding":
                "MRI findings are suggestive of Meningioma.",

            "severity":
                "Moderate",

            "recommendation":
                "Specialist consultation is recommended. Follow-up imaging may be required."

        },

        "pituitary": {

            "finding":
                "MRI findings are suggestive of a Pituitary Tumor.",

            "severity":
                "Moderate",

            "recommendation":
                "Endocrinology and neurosurgical evaluation are recommended."

        },

        "notumor": {

            "finding":
                "No brain tumor was detected on this MRI image.",

            "severity":
                "Normal",

            "recommendation":
                "Continue routine clinical follow-up if symptoms persist."

        }

    },

    "CT": {

    },

    "XRAY": {

    }

}
