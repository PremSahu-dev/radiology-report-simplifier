"""
metadata.py

Extracts AI prediction metadata.
"""


class MetadataExtractor:


    def extract(
        self,
        ai_result,
        modality
    ):
        """
        Extract metadata from
        MRI/X-Ray AI output.
        """


        data = {

            "modality": modality.upper(),

            "prediction": "",

            "confidence": 0

        }


        # -------------------------
        # MRI
        # -------------------------

        if "prediction" in ai_result:


            data["prediction"] = (
                ai_result["prediction"]
            )


            data["confidence"] = (
                ai_result.get(
                    "confidence",
                    0
                )
            )


        # -------------------------
        # X-Ray
        # -------------------------

        elif "top_prediction" in ai_result:


            top = ai_result[
                "top_prediction"
            ]


            data["prediction"] = (
                top.get(
                    "disease",
                    ""
                )
            )


            data["confidence"] = (
                top.get(
                    "confidence",
                    0
                )
            )


        return data