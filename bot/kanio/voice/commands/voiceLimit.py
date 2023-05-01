import nextcord
from nextcord import PartialInteractionMessage, WebhookMessage
from nextcord.ext import commands
from src.logger.logger import Logging
from src.settings.voice import permissions


class VoiceLimit(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(
        name="kanio-voice-limit",
        description="Change the limit voice from the voice",
        force_global=True
    )
    async def voice_limit(
            self,
            ctx: nextcord.Interaction,
            limit: int = nextcord.SlashOption(
                description="The limit you want to set. Set 0 to disable the limit.",
                required=True
            )
    ) -> PartialInteractionMessage | WebhookMessage:

        """
        Attributes
        ----------
        :param ctx:
        :param limit:
        :return: None
        ----------
        """

        Logging().info(f"Command :: kanio-voice-limit :: {ctx.guild.name} :: {ctx.user}")

        if not await permissions.check(ctx):
            return await ctx.send("You have no permission to do that.", ephemeral=True)

        if limit < 0 or limit > 99:
            return await ctx.send("The channel must be between 0 and 99.", ephemeral=True)

        await ctx.user.voice.channel.edit(
            user_limit=limit
        )
        await ctx.send(f"User limit changed to {limit}", ephemeral=True)


def setup(bot):
    bot.add_cog(VoiceLimit(bot))
