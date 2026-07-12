"""
sentence_simplifier.py

Simplifies individual medical sentences.
"""


from glossary.glossary import Glossary

from simplifier.postprocess import PostProcessor

from simplifier.huggingface_model import HuggingFaceModel

from simplifier.prompts_builder import PromptBuilder



class SentenceSimplifier:
    """
    Converts medical sentences into
    simple patient-friendly sentences.
    """



    def __init__(
        self,
        use_model=False,
        model_name=None
    ):


        self.glossary = Glossary()

        self.postprocessor = PostProcessor()

        self.prompt_builder = PromptBuilder()


        self.use_model = use_model


        self.model = None


        if use_model:

            self.model = HuggingFaceModel(
                model_name
            )



    def simplify(
        self,
        sentence
    ):
        """
        Simplify a single sentence.

        Parameters
        ----------
        sentence : str


        Returns
        -------
        str
        """



        if not sentence:

            return ""



        # --------------------------------
        # Optional Transformer model
        # --------------------------------

        if self.use_model:


            prompt = self.prompt_builder.build_sentence_prompt(
                sentence
            )


            result = self.model.generate(
                prompt
            )


            return self.postprocessor.clean(
                result
            )



        # --------------------------------
        # Rule based simplification
        # --------------------------------


        words = sentence.split()


        simplified_words = []


        for word in words:


            cleaned_word = word.strip(
                ".,!?;"
            )


            meaning = self.glossary.simplify_word(
                cleaned_word
            )


            if meaning != cleaned_word:

                simplified_words.append(
                    meaning
                )

            else:

                simplified_words.append(
                    word
                )



        result = " ".join(
            simplified_words
        )


        return self.postprocessor.clean(
            result
        )