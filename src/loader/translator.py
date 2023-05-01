import json


class GetTranslator:
    def __init__(self):
        with open("resources/translator/supportedLanguages.json", "r") as c:
            self.__config = json.load(c)

    def get_supported_languages(self) -> list:
        return self.__config["supported_languages"]

    def get_reaction_language(self) -> list:
        return self.__config["reaction_translate"]
