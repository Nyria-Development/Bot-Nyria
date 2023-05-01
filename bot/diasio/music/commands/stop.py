import mafic
import nextcord
from mafic import Node
from nextcord import PartialInteractionMessage, WebhookMessage
from nextcord.ext import commands
from src.logger.logger import Logging


class Stop(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(
        name="diasio-music-stop",
        description="Stop the playing song",
        guild_ids=[981547050770505819, 1032632067307085955]
    )
    async def stop(
            self,
            ctx: nextcord.Interaction
    ) -> PartialInteractionMessage | WebhookMessage:

        """

        :param ctx:
        :return:
        """

        Logging().info(f"Command :: diasio-music-stop :: {ctx.guild.name} :: {ctx.user}")

        voice = ctx.user.voice
        node: Node = mafic.NodePool.get_node(guild_id=ctx.guild.id, endpoint="MAIN")
        player = node.get_player(ctx.guild.id)

        if voice is None:
            return await ctx.send("You are currently not connected to a voice channel.", ephemeral=True)

        if player is None:
            return await ctx.send("The music bot is not connected", ephemeral=True)

        await player.destroy()
        await ctx.send("Stopped")


def setup(bot):
    bot.add_cog(Stop(bot))
