import nextcord
from nextcord.ext import commands


class ToggleCommands(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(
        name="pyrio-toggle-command",
        description="Toggle a command to activate or deactivate them.",
        force_global=True,
        default_member_permissions=8
    )
    async def toggle_command(
            self,
            ctx: nextcord.Interaction,
            command=nextcord.SlashOption(choices=[]),
            state=nextcord.SlashOption(choices=[])
    ) -> None:

        """
        Attributes
        ----------
        :param ctx:
        :param command:
        :param state:
        :return: None
        ----------
        """

        pass


def setup(bot):
    bot.add_cog(ToggleCommands(bot))
