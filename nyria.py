import nextcord
from nextcord.ext import commands
from src.loader.jsonLoader import Tokens
import os
from database.check import Check


class Nyria(commands.Bot):
    def __init__(self):
        super().__init__(intents=nextcord.Intents.all())

        # load config
        self.__token = Tokens().token()

        # get all intents
        self.remove_command("help")
        print("Requirements loaded")
        print("Member Intents: ", self.intents.members)
        print("guild Intents: ", self.intents.guilds)
        print("message content Intents: ", self.intents.message_content)
        print(self.intents.value) #3243773 (all) 3243773(defult)

        # load all cogs
        for root, dirs, files in os.walk("bot"):
            for name in files:
                if str(root).endswith("__pycache__"):
                    continue
                self.load_extension(os.path.join(root, name).replace("\\", ".")[:-3])

        self.run(self.__token)


if __name__ == "__main__":
    # check if database faultless
    Check().inspect()
    # start the bot
    Nyria()
