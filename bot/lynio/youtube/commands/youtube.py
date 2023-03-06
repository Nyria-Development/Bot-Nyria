import googleapiclient.discovery
from src.loader.jsonLoader import Tokens
from nextcord.ext import commands
import nextcord


class YouTube(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.api_key = Tokens().youtube()


def setup(bot):
    bot.add_cog(YouTube(bot))
