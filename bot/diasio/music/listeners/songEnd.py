import mafic
import nextcord
from mafic import TrackEndEvent
from nextcord.ext import commands
from src.settings.music import settingQueue


class SongEnds(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_track_end(self, event: TrackEndEvent):
        player = event.player

        next_song = await settingQueue.get_song_name(
            guild_id=event.player.guild.id
        )
        if not next_song:
            return

        tracks = await player.fetch_tracks(query=next_song)
        await player.play(tracks[0])


def setup(bot):
    bot.add_cog(SongEnds(bot))
