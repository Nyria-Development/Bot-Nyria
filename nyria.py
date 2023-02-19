from nextcord.ext import commands
import json
import os
from database.check import Check


class Nyria(commands.Bot):
    def __init__(self):
        super().__init__()

        # load config
        with open("config.json", "r") as c:
            self.__config = json.load(c)
            self.__token = self.__config["token"]
        print("Config loaded")

        # get all intents
        self.intents.all()
        self.remove_command("help")
        print("Requirements loaded")

        # load all cogs
        for root, dirs, files in os.walk("bot"):
            for name in files:

                if str(root).endswith("__pycache__"):
                    continue
                self.load_extension(os.path.join(root, name).replace("/", ".")[:-3])

        self.run(self.__token)


if __name__ == "__main__":
    # check if database faultless
    Check().inspect()
    # start the bot
    Nyria()
