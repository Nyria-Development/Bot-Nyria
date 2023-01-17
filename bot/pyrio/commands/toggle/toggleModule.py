import nextcord
from nextcord.ext import commands


class ToggleModule(commands.Cog):
    def __init__(self, bot: nextcord.Interaction):
        self.bot = bot

    @nextcord.slash_command(
        name="pyrio-toggle-module",
        description="Toggle any module off or on.",
        force_global=True,
        default_member_permissions=8
    )
    async def toggle_module(self, ctx: nextcord.Interaction):
        pass


def setup(bot):
    bot.add_cog(ToggleModule(bot))
