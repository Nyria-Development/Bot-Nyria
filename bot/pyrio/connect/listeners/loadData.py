from nextcord.ext import commands
from src.dictionaries import logs


class LoadData(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_connect(self):
        await logs.load_log_channels()


def setup(bot):
    bot.add_cog(LoadData(bot))
