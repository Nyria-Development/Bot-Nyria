import nextcord
from nextcord.ext import commands


class Unban(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(
        name="metrio-unban",
        description="Unban a member",
        force_global=True,
        default_member_permissions=8
    )
    async def unban(self, ctx: nextcord.Interaction):
        pass


def setup(bot):
    bot.add_cog(Unban(bot))
