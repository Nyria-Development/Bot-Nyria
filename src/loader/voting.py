import json


class GetVoting:
    def __init__(self):
        with open("resources/voting/voting.json", "r") as c:
            self.__config = json.load(c)

    def get_voting(self) -> list:
        return self.__config["voting_numbers"]
