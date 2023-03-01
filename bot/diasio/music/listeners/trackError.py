import wavelink
from nextcord.ext import commands


class MusicTrackError(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_wavelink_track_exception(self, player: wavelink.Player, track: wavelink.Track, error):
        print(error)

    @commands.Cog.listener()
    async def on_wavelink_track_stuck(self, player: wavelink.Player, track: wavelink.Track, threshold):
        pass


def setup(bot):
    bot.add_cog(MusicTrackError(bot))
