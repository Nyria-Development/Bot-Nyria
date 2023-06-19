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

from nextcord.ext import commands

from bot.kanio.voice.listeners.startupCleaner import startup_voice_cleaner
from bot.metrio.logs.listeners.logsMemoryCache import logs_memory_cache
from bot.pyrio.ready.listeners.ready import ready


class OnReady(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self) -> None:
        """
        Attributes
        ----------
        :return:
        ----------
        """

        # bot/metrio/logs/listeners/logsMemoryCache.py
        await logs_memory_cache(bot=self.bot)

        # bot/kanio/voice/listeners/startupCleaner.py
        await startup_voice_cleaner(self.bot)

        # bot/pyrio/ready/listeners/ready.py
        await ready(self.bot.user)


def setup(bot):
    bot.add_cog(OnReady(bot))
