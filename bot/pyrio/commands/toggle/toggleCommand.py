import nextcord
from nextcord.ext import commands


class ToggleCommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(
        name="pyrio-toggle-command",
        description="Toggle any command on or off.",
        force_global=True,
        default_member_permissions=8
    )
    async def toggle_command(self, ctx: nextcord.Interaction):
        pass


def setup(bot):
    bot.add_cog(ToggleCommand(bot))
