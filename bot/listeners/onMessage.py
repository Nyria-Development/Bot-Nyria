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

from bot.metrio.logs.listeners.messages import on_message_log, on_message_edit_log, on_message_delete_log


class OnMessage(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(
            self,
            message
    ) -> None:
        """
        Attributes
        ----------
        :param message:
        :return:
        ----------
        """

        # bot/listeners/onMessage.py
        await on_message_log(self.bot, message)

    @commands.Cog.listener()
    async def on_message_delete(
            self,
            message: nextcord.Message
    ) -> None:
        """
        Attributes
        ----------
        :param message:
        :return:
        ----------
        """

        # bot/listeners/onMessage.py
        await on_message_delete_log(self.bot, message)

    @commands.Cog.listener()
    async def on_message_edit(
            self,
            before: nextcord.Message,
            after: nextcord.Message
    ) -> None:
        """
        Attributes
        ----------
        :param after:
        :param before:
        :return:
        ----------
        """

        # bot/listeners/onMessage.py
        await on_message_edit_log(self.bot, before=before, after=after)


def setup(bot):
    bot.add_cog(OnMessage(bot))
