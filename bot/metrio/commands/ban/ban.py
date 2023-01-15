import nextcord
from nextcord.ext import commands


class Ban(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(
        name="metrio-ban",
        description="Ban a member",
        force_global=True
    )
    async def ban(self, ctx: nextcord.Interaction):
        pass


def setup(bot):
    bot.add_cog(Ban(bot))
