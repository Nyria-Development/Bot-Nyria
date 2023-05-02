import nextcord
import mafic
from mafic import Node
from nextcord import PartialInteractionMessage, WebhookMessage
from nextcord.ext import commands
from src.logger.logger import Logging


class Pause(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(
        name="diasio-music-pause",
        description="Pause the song in voice channel.",
        guild_ids=[981547050770505819, 1032632067307085955]
    )
    async def pause(
            self,
            ctx: nextcord.Interaction
    ) -> PartialInteractionMessage | WebhookMessage:

        """
        Attributes
        ----------
        :param ctx:
        :return: None
        ----------
        """

        Logging().info(f"Command :: diasio-music-pause :: {ctx.guild.name} :: {ctx.user}")

        voice = ctx.user.voice
        node: Node = mafic.NodePool.get_node(guild_id=ctx.guild.id, endpoint="MAIN")
        player = node.get_player(ctx.guild.id)

        if voice is None:
            return await ctx.send("You are not in a voice channel. Please connect.", ephemeral=True)

        if player is None:
            return await ctx.send("The bot doesn't play in the voice channel.", ephemeral=True)

        if player.paused:
            return await ctx.send("The bot is already paused.", ephemeral=True)

        await player.pause()
        await ctx.send("Music paused")


def setup(bot):
    bot.add_cog(Pause(bot))
