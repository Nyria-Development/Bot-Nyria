from nextcord.ext import commands
import wavelink
from src.loader.jsonLoader import Tokens
import atexit


class MusicNodeConnection(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.host, self.port, self.password = Tokens().wavelink()

        self.bot.loop.create_task(self.connect_node())

    async def connect_node(self):
        try:
            await self.bot.wait_until_ready()
            res = await wavelink.NodePool.create_node(
                bot=self.bot,
                host=self.host,
                port=self.port,
                password=self.password
            )
            print("Node connected")
        except wavelink.WavelinkError:
            print("Can't connect to Node")


def setup(bot):
    bot.add_cog(MusicNodeConnection(bot))
