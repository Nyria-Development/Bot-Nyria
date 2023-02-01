import json


class JsonLoader:
    def __init__(self):
        with open("config.json", "r") as c:
            self.__config = json.load(c)
            self.__token = self.__config["token"]
            self.__host = self.__config["wavelink"]["host"]
            self.__port = self.__config["wavelink"]["port"]
            self.__password = self.__config["wavelink"]["password"]
            self.m_host = self.__config["mariadb"]["host"]
            self.m_user = self.__config["mariadb"]["user"]
            self.m_password = self.__config["mariadb"]["password"]
            self.m_database = self.__config["mariadb"]["database"]
