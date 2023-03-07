import nextcord
from nextcord.ext import commands
from src.templates import embeds


class setLogChannel(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(
        name="set_log_channel",
        description="Ban a member",
        force_global=True,
        default_member_permissions=8
    )
    async def set_log_channel(self, ctx: nextcord.Interaction):
        print(ctx)


def setup(bot):
    bot.add_cog(setLogChannel(bot))
