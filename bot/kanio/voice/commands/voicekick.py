import nextcord
from nextcord import PartialInteractionMessage, WebhookMessage
from nextcord.ext import commands
from src.logger.logger import Logging
from src.settings.voice import permissions


class VoiceKick(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(
        name="kanio-voice-kick",
        description="Kick any user from your voice",
        force_global=True
    )
    async def voice_kick(
            self,
            ctx: nextcord.Interaction,
            user: nextcord.Member
    ) -> PartialInteractionMessage | WebhookMessage:

        """
        Attributes
        ----------
        :param ctx:
        :param user:
        :return: None
        ----------
        """

        Logging().info(f"Command :: kanio-voice-kick :: {ctx.guild.name} :: {ctx.user}")

        if not await permissions.check(ctx):
            return await ctx.send("You have no permission to do that.", ephemeral=True)

        if ctx.user == user:
            return await ctx.send("You can't ban yourself.", ephemeral=True)

        if user.voice is not None or ctx.user.voice != user.voice:
            return await ctx.send(f"The user {user} is not connected or in the same voice.", ephemeral=True)

        await user.disconnect()
        await ctx.send(f"The user {user} was kicked from voice.")


def setup(bot):
    bot.add_cog(VoiceKick(bot))
