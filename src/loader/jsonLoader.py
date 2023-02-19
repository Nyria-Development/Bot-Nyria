import json


class JsonLoader:
    def __init__(self):
        with open("config.json", "r") as c:
            self.__config = json.load(c)

    async def token(self):
        return self.__config["token"]

    async def wavelink(self):
        return self.__config["wavelink"]["host"], self.__config["wavelink"]["port"], self.__config["wavelink"]["password"]

    def maria_db(self):
        return self.__config["mariadb"]["host"], self.__config["mariadb"]["user"], self.__config["mariadb"]["password"], self.__config["mariadb"]["database"]

    async def get_welcome_colors(self):
        colors: dict = self.__config["kanio"]["welcome_colors"][0]
        return colors

    async def get_welcome_backgrounds(self):
        bgs: dict = self.__config["kanio"]["welcome_bg"][0]
        return bgs

    async def get_voting_numbers(self):
        nums: dict = self.__config["kanio"]["voting_numbers"][0]
        return nums

    async def get_supported_languages(self):
        return self.__config["diasio"]["supported_languages"][0]
