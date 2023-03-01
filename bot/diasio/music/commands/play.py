import nextcord
import wavelink
from nextcord.ext import commands
from src.templates import embeds
from database.query import Query


class Play(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.database = Query(
            pool_name="play_music",
            pool_size=2
        )

    @nextcord.slash_command(
        name="diasio-play",
        description="Play your favourite song in the voice channel.",
        force_global=True
    )
    async def play(self, ctx: nextcord.Interaction, search: str):
        await ctx.response.defer()

        if search.startswith("https://"):
            if not search.startswith("https://www.youtube.com") or search.startswith("https://youtu.be"):
                return await ctx.send("You can only play youtube links.", ephemeral=True)

        node = wavelink.NodePool.get_node()
        player = node.get_player(ctx.guild)
        embed_play = embeds.TemplateEmbed(
            bot=self.bot,
            ctx=ctx,
            description="Fun | diasio",
            color=nextcord.Color.dark_gold()
        )

        if player is None:
            player = await ctx.user.voice.channel.connect(cls=wavelink.Player)

        if not player.is_playing():
            try:
                query = await wavelink.YouTubeTrack.search(query=search, return_first=True)
            except wavelink.LavalinkException:
                return await ctx.send("Track not found.")

            embed_play.add_field(name="Song name", value=query.title, inline=False)
            embed_play.add_field(name="Auther", value=query.author)
            embed_play.add_field(name="Length", value=query.length)
            embed_play.add_field(name="Url", value=query.uri, inline=False)
            embed_play.set_thumbnail(url=query.thumbnail)

            await player.play(query)
            return await ctx.send(embed=embed_play)

        if player.is_playing():
            tracks_ids = self.database.execute(
                query="SELECT tracksId FROM music WHERE serverId=%s",
                data=[int(ctx.guild.id)]
            )

            if not tracks_ids and player.is_playing():
                self.database.execute(
                    query="INSERT INTO music (serverId, tracksId, trackName) VALUE (%s,%s,%s)",
                    data=[int(ctx.guild.id), int(50), str(search)]
                )
                return await ctx.send("Song added to queue.")

            min_value = min(tracks_ids)
            if min_value[0] < 1:
                return await ctx.send("Can't add to queue, because there are not many songs in the queue.", ephemeral=True)

            # TODO SQL injection?
            self.database.execute(
                query="INSERT INTO music (serverId, tracksId, trackName) VALUE (%s,%s,%s)",
                data=[int(ctx.guild.id), int(min_value[0] - 1), str(search)]
            )
            return await ctx.send("Song added to queue.")


def setup(bot):
    bot.add_cog(Play(bot))
