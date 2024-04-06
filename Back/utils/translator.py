from googletrans import Translator

class CustomTranslator:
    def __init__(self):
        self.translator = Translator()

    def translate_text(self, text, dest_language='en'):
        try:
            translation = self.translator.translate(text, dest=dest_language)
            return translation.text
        except Exception as e:
            print("Error during translation:", e)
            return text  # Devuelve el texto original si ocurre un error

