import nextcord
from nextcord.ext import commands
from src.loader.jsonLoader import Pyrio


class ToggleModule(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(
        name="pyrio-toggle-module",
        description="Toggle a module to activate or deactivate them.",
        force_global=True,
        default_member_permissions=8
    )
    async def toggle_module(
            self,
            ctx: nextcord.Interaction,
            module=nextcord.SlashOption(choices=[]),
            state=nextcord.SlashOption(choices=Pyrio().get_state())
    ) -> None:

        """
        Attributes
        ----------
        :param ctx:
        :param module:
        :param state:
        :return: None
        ----------
        """

        pass


def setup(bot):
    bot.add_cog(ToggleModule(bot))
