# All Rights Reserved
# Copyright (c) 2023 Nyria
#
# This code, including all accompanying software, documentation, and related materials, is the exclusive property
# of Nyria. All rights are reserved.
#
# Any use, reproduction, distribution, or modification of the code without the express written
# permission of Nyria is strictly prohibited.
#
# No warranty is provided for the code, and Nyria shall not be liable for any claims, damages,
# or other liability arising from the use or inability to use the code.

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
