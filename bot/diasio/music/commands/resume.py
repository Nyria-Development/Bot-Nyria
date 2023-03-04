import nextcord
from nextcord.ext import commands
import wavelink


class Resume(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(
        name="diasio-music-resume",
        description="Resume song in voice channel.",
        force_global=True
    )
    async def resume(self, ctx: nextcord.Interaction):
        node = wavelink.NodePool.get_node()
        player = node.get_player(ctx.guild)

        if not player.is_paused():
            return await ctx.send("The song is playing")

        await player.resume()
        await ctx.send("The song is playing again")


def setup(bot):
    bot.add_cog(Resume(bot))
