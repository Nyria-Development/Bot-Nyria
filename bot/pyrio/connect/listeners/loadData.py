from nextcord.ext import commands
from src.dictionaries import logs
from src.dictionaries import level


class LoadData(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_connect(self):
        await logs.load_log_channels()
        await level.load_leveling_servers()


def setup(bot):
    bot.add_cog(LoadData(bot))
