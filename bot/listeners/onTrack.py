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

import nextcord
from mafic import TrackEndEvent
from nextcord.ext import commands

from bot.diasio.music.listeners.songEnd import on_track_end


class OnTrack(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_track_end(
            self,
            event: TrackEndEvent
    ) -> None:
        """
        Attributes
        ----------
        :param event:
        :return:
        ----------
        """

        # bot/diasio/music/listeners/songEnd.py
        await on_track_end(event)


def setup(bot):
    bot.add_cog(OnTrack(bot))
