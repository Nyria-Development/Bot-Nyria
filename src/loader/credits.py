import json


class GetCredits:
    def __init__(self):
        with open("resources/credits/credits.json", "r") as c:
            self.__config = json.load(c)

    def get_credits(self):
        return self.__config
