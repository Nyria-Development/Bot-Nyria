import nextcord.ext
from nextcord.ext import commands
import wavelink


class Volume(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(
        name="diasio-music-volume",
        description="Set the volume of the bot.",
        guild_ids=[1032632067307085955, 1043477521473212547]
    )
    async def volume(self, ctx: nextcord.Interaction, volume: int):
        if volume > 100 or volume < 0:
            return await ctx.send("Volume can only be specified between 0 and 100", ephemeral=True)

        node = wavelink.NodePool.get_node()
        player = node.get_player(ctx.guild)

        if player is None:
            return await ctx.send("The bot is not in permissions channel.", ephemeral=True)

        await player.set_volume(volume)
        await ctx.send(f"Volume set by: {volume}", ephemeral=True)


def setup(bot):
    bot.add_cog(Volume(bot))
