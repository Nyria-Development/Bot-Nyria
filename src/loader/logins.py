import json


class GetLogin:
    def __init__(self):
        with open("resources/config/login.json", "r") as c:
            self.__config = json.load(c)

    def get_token(self) -> str:
        return self.__config["token"]

    def get_mariadb(self) -> tuple[str, str, str, str]:
        return self.__config["mariadb"]["host"], self.__config["mariadb"]["user"], self.__config["mariadb"]["password"], self.__config["mariadb"]["database"]

    def get_lavalink(self) -> tuple[str, int, str]:
        return self.__config["lavalink"]["host"], self.__config["lavalink"]["port"], self.__config["lavalink"]["password"]
