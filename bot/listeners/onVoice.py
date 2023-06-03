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
from nextcord.ext import commands

from bot.diasio.music.listeners.autoLeave import auto_leave
from bot.kanio.voice.listeners.manager import voice_manager


class OnVoice(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_voice_state_update(
            self, member: nextcord.Member,
            before: nextcord.VoiceState,
            after: nextcord.VoiceState
    ) -> None:
        """
        Attributes
        ----------
        :param after:
        :param before:
        :param member:
        :return: None
        ----------
        """

        # bot/diasio/music/listeners/autoLeave.py
        await auto_leave(member, before, after)
        # bot/kanio/voice/listeners/manager.py
        await voice_manager(member, before, after)


def setup(bot):
    bot.add_cog(OnVoice(bot))
