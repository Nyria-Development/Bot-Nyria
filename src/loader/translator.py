# All Rights Reserved
# Copyright (c) 2023 Nyria
#
# This code, including all accompanying software, documentation, and related materials, is the exclusive property
# of Nyria. All rights are reserved.
#
# Any use, reproduction, distribution, or modification of the code without the express written
# permission of Nyria is strictly prohibited.
#
# No warranty is provided for the code, and Nyria shall not be liable for any claims, damages,
# or other liability arising from the use or inability to use the code.

import json


class GetTranslator:
    def __init__(self):
        with open("resources/translator/supportedLanguages.json", "r") as c:
            self.__config = json.load(c)

    def get_supported_languages(self) -> list:
        return self.__config["supported_languages"]

    def get_reaction_language(self) -> list:
        return self.__config["reaction_translate"]
