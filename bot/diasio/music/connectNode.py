from nextcord.ext import commands
import wavelink
import json


class ConnectNode(commands.Cog):
    def __init__(self, bot: commands.Bot):
        with open("config.json", "r") as f:
            config = json.load(f)
            self.bot = bot
            self.host = config["wavelink"]["host"]
            self.port = config["wavelink"]["port"]
            self.password = config["wavelink"]["password"]

            self.bot.loop.create_task(self.connect_node())

    async def connect_node(self):
        try:
            await self.bot.wait_until_ready()
            await wavelink.NodePool.create_node(
                bot=self.bot,
                host=self.host,
                port=self.port,
                password=self.password
            )
            print("Node connected")
        except wavelink.WavelinkError:
            print("Can't connect to Node")


def setup(bot):
    bot.add_cog(ConnectNode(bot))
