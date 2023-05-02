import nextcord
from nextcord import PartialInteractionMessage, WebhookMessage
from nextcord.ext import commands
from src.logger.logger import Logging
from src.settings.voice import permissions


class VoiceUnban(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(
        name="kanio-voice-unban",
        description="Unban banned member from your voice",
        force_global=True
    )
    async def voice_unban(
            self,
            ctx: nextcord.Interaction,
            user: nextcord.Member = nextcord.SlashOption(
                description="The user you want to unban."
            )
    ) -> PartialInteractionMessage | WebhookMessage:

        """
        Attributes
        ----------
        :param ctx:
        :param user
        :return: None
        ----------
        """

        Logging().info(f"Command :: kanio-voice-ban :: {ctx.guild.name} :: {ctx.user}")

        if not await permissions.check(ctx):
            return await ctx.send("You have no permission to do that.", ephemeral=True)

        if ctx.user == user:
            return await ctx.send("You can't banned or unbanned, because you are the owner.", ephemeral=True)

        await ctx.user.voice.channel.set_permissions(
            target=user,
            view_channel=True
        )
        await ctx.send(f"You have unbanned the user {user} from your voice.", ephemeral=True)


def setup(bot):
    bot.add_cog(VoiceUnban(bot))
