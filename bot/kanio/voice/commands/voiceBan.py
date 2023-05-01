import nextcord
from nextcord import PartialInteractionMessage, WebhookMessage
from nextcord.ext import commands
from src.logger.logger import Logging
from src.settings.voice import permissions


class VoiceBan(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(
        name="kanio-voice-ban",
        description="Ban any member from your voice.",
        force_global=True
    )
    async def voice_ban(
            self,
            ctx: nextcord.Interaction,
            user: nextcord.Member = nextcord.SlashOption(
                description="The member you want to ban."
            )
    ) -> PartialInteractionMessage | WebhookMessage:

        """
        Attributes
        ----------
        :param ctx:
        :param user:
        :return: None
        ----------
        """

        Logging().info(f"Command :: kanio-voice-ban :: {ctx.guild.name} :: {ctx.user}")

        if not await permissions.check(ctx):
            return await ctx.send("You have no permission to do that.", ephemeral=True)

        if ctx.user == user:
            return await ctx.send("You can't ban yourself.", ephemeral=True)

        if user.voice is not None and ctx.user.voice == user.voice:
            await user.disconnect()

        await ctx.user.voice.channel.set_permissions(
            target=user,
            view_channel=False
        )
        await ctx.send(f"You have banned the user {user} from your voice.", ephemeral=True)


def setup(bot):
    bot.add_cog(VoiceBan(bot))
