import json


class JsonLoader:
    def __init__(self):
        with open("config.json", "r") as c:
            self.__config = json.load(c)

    async def token(self):
        return self.__config["token"]

    async def wavelink(self):
        return self.__config["wavelink"]["host"], self.__config["wavelink"]["port"], self.__config["wavelink"]["password"]

    async def maria_db(self):
        return self.__config["mariadb"]["host"], self.__config["mariadb"]["user"], self.__config["mariadb"]["password"], self.__config["mariadb"]["database"]
