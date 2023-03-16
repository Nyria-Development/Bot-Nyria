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


class Pyrio:
    def __init__(self):
        with open("resources/config/pyrio.json", "r") as c:
            self.__config = json.load(c)

    def get_state(self) -> list:
        state = self.__config["state"][0]
        return state


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

    def get_minecraft_server_types(self):
        return self.__config["minecraft_server_type"]


class Plirio:
    def __init__(self):
        with open("resources/config/plirio.json", "r") as c:
            self.__config = json.load(c)

    def credits(self):
        return self.__config


class Leveling:
    def __init__(self):
        with open("resources/information/leveling.json", "r") as c:
            self.file = c
            self.__config = json.load(c)

    def get_levels(self):
        return self.__config

class LevelRoles:
    def __init__(self):
        with open("resources/information/levelRoles.json", "r") as c:
            self.file = c
            self.__config = json.load(c)

    def get_Roles(self):
        return self.__config


class Commands:
    def __init__(self):
        with open("resources/config/commands.json", "r") as c:
            self.file = c
            self.__config = json.load(c)

    def get_commands(self):
        return self.__config


