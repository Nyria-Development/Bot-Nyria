import mafic
import atexit
from nextcord.ext import commands
from src.logger.logger import Logging
from src.loader.logins import GetLogin


class MusicNodeManager(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.pool = mafic.NodePool(self.bot)

        self.loop = self.bot.loop.create_task(self.register_node())

    async def register_node(self):
        host, port, password = GetLogin().get_lavalink()

        await self.pool.create_node(
            host=host,
            port=port,
            label="MAIN",
            password=password
        )
        Logging().info("Music Node connected")


def setup(bot):
    bot.add_cog(MusicNodeManager(bot))
