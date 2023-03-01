import wavelink
from nextcord.ext import commands
from database.query import Query


class Queue(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.database = Query(
            pool_name="queue_music",
            pool_size=2
        )

    @commands.Cog.listener()
    async def on_wavelink_track_end(self, player: wavelink.Player, track: wavelink.Track, reason):
        track_ids = self.database.execute(
            "SELECT tracksId FROM music WHERE serverId=%s",
            data=[int(player.guild.id)]
        )

        if not track_ids:
            return

        max_value = max(track_ids)
        track_name = self.database.execute(
            query="SELECT trackName FROM music WHERE serverId=%s AND tracksId=%s",
            data=[int(player.guild.id), int(max_value[0])]
        )

        query = await wavelink.YouTubeTrack.search(query=track_name[0][0], return_first=True)
        self.database.execute(
            query="DELETE FROM music WHERE tracksId=%s AND serverId=%s",
            data=[int(max_value[0]), int(player.guild.id)]
        )
        await player.play(query)


def setup(bot):
    bot.add_cog(Queue(bot))
