import os
import nextcord
import multiprocessing
from api.apiServer import ApiServer
from nextcord.ext import commands
from src.loader.logins import GetLogin
from src.logger.logger import Logging
from src.database.core.register import Register
from src.services.system import Os


class Nyria(commands.Bot):
    def __init__(self):
        super().__init__(
            intents=nextcord.Intents.all()
        )

        # check run as root
        Os.check_permissions()

        # load the token from config
        self.__token = GetLogin().get_token()
        Logging().info("Token loaded")

        # remove help command
        self.remove_command("help")
        Logging().info("Build-in help command removed")

        # load all cogs
        for root, dirs, files in os.walk("bot"):
            for name in files:
                if str(root).endswith("__pycache__"):
                    continue

                self.load_extension(os.path.join(root, name).replace("/", ".")[:-3])

        Logging().info("All cogs loaded")

        multiprocessing.Process(target=ApiServer.run_server).start()
        Logging().info("Api started")

        # run the bot
        self.run(self.__token)


if __name__ == "__main__":
    # register all tables from the database
    Register.register()
    # Create the instance of nyria to run them
    Nyria()
