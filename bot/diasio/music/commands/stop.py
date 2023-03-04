import nextcord
from nextcord.ext import commands
import wavelink


class Stop(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(
        name="diasio-music-stop",
        description="Stop playing music in the voice channel.",
        guild_ids=[1032632067307085955]
    )
    async def music_stop(self, ctx: nextcord.Interaction):
        node = wavelink.NodePool.get_node()
        player = node.get_player(ctx.guild)

        if player is None:
            return await ctx.send("No song is playing in the voice channel.", ephemeral=True)

        if ctx.user.voice.channel != player.channel:
            return await ctx.send("You are not in the current voice channel")

        await player.disconnect()
        await ctx.send("Bot is disconnected.", ephemeral=True)


def setup(bot):
    bot.add_cog(Stop(bot))
