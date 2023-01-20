import nextcord
from nextcord.ext import commands
import wavelink
from templates import embeds


class Play(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(
        name="diasio-music-play",
        description="Play your favourite music in a voice channel.",
        guild_ids=[1043477521473212547, 1032632067307085955]
    )
    async def play(self, ctx: nextcord.Interaction, url: str):
        await ctx.response.defer()

        if url.startswith("http"):
            if not url.startswith("https://www.youtube.com") or url.startswith("https://youtu.be"):
                return await ctx.send("You can only play YouTube links.", ephemeral=True)

        node = wavelink.NodePool.get_node()

        try:
            search = await wavelink.YouTubeTrack.search(query=url, return_first=True)
        except wavelink.LavalinkException:
            return await ctx.send("Track not found.")

        player: wavelink.Player = node.get_player(ctx.guild)

        if player is None:
            player = await ctx.user.voice.channel.connect(cls=wavelink.Player)

        if not player.is_playing():
            await player.play(search)

            embed_play = embeds.TemplateEmbed(
                bot=self.bot,
                ctx=ctx,
                description="Fun | Diasio",
                color=nextcord.Color.dark_gold()

            )
            embed_play.set_thumbnail(url=search.thumbnail)
            embed_play.add_field(name="Now playing", value=str(search.title), inline=False)
            embed_play.add_field(name="Volume", value=str(player.volume))
            embed_play.add_field(name="Length", value=str(search.length.real))
            embed_play.add_field(name="Author", value=str(search.author))
            embed_play.add_field(name="Url:", value=str(search.info["uri"]), inline=False)

            await ctx.send(embed=embed_play)


def setup(bot):
    bot.add_cog(Play(bot))
