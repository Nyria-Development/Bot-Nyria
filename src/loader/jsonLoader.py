import json


class Tokens:
    def __init__(self):
        with open("resources/config/tokens.json", "r") as c:
            self.__config = json.load(c)

    def token(self):
        return self.__config["token"]

    def wavelink(self):
        return self.__config["wavelink"]["host"], self.__config["wavelink"]["port"], self.__config["wavelink"][
            "password"]

    def maria_db(self):
        return self.__config["mariadb"]["host"], self.__config["mariadb"]["user"], self.__config["mariadb"]["password"], \
            self.__config["mariadb"]["database"]

    def youtube(self):
        return self.__config["social_media"]["youtube"]


class Kanio:
    def __init__(self):
        with open("resources/config/kanio.json", "r") as c:
            self.__config = json.load(c)

    def get_voting_numbers(self):
        nums: dict = self.__config["voting_numbers"][0]
        return nums


class Diasio:
    def __init__(self):
        with open("resources/config/diasio.json", "r") as c:
            self.__config = json.load(c)

    def get_supported_languages(self):
        return self.__config["supported_languages"][0]
