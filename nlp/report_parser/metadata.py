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

        elif "prediction" in ai_result:

        

            prediction = ai_result["prediction"]

            confidence = ai_result["confidence"]
            


            data["prediction"] = (
                ai_result.get(
                    "disease",
                    ""
                )
            )


            data["confidence"] = (
                ai_result.get(
                    "confidence",
                    0
                )
            )


        return data