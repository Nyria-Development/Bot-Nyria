import nextcord.ext
from nextcord.ext import commands
import wavelink


class Stop(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(
        name="diasio-music-stop",
        description="Stop playing songs in voice channel",
        guild_ids=[1043477521473212547, 1032632067307085955]
    )
    async def stop(self, ctx: nextcord.Interaction):
        node = wavelink.NodePool.get_node()
        player = node.get_player(ctx.guild)

        if player is None:
            return await ctx.send("The bot is not in voice channel.", ephemeral=True)

        await player.disconnect()
        await ctx.send("The bot is disconnected.", ephemeral=True)


def setup(bot):
    bot.add_cog(Stop(bot))
    