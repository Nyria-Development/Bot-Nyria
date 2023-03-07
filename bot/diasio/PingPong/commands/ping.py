import nextcord
from nextcord.ext import commands
import random
from src.templates import embeds


class PingPong(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        test = 0

    @nextcord.slash_command(name="ping", description="Try it ", force_global=True)
    async def ping(self, ctx: nextcord.Interaction):
        await ctx.send("Pong!")


def setup(bot):
    bot.add_cog(PingPong(bot))
