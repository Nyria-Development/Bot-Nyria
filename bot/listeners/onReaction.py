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

from bot.diasio.translator.listeners.reaction import translate_reaction
from bot.metrio.logs.listeners.reaction import on_raw_reaction_add_log, on_raw_reaction_remove_log


class OnReaction(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_raw_reaction_add(
            self,
            payload: nextcord.RawReactionActionEvent
    ) -> None:
        """
        Attributes
        ----------
        :param payload:
        :return:
        ----------
        """

        # bot/diasio/translator/listeners/reaction.py
        await translate_reaction(self.bot, payload)

        # bot/metrio/logs/listeners/reaction.py
        await on_raw_reaction_add_log(self.bot, payload)

    @commands.Cog.listener()
    async def on_raw_reaction_remove(
            self,
            payload: nextcord.RawReactionActionEvent
    ) -> None:
        """
        Attributes
        ----------
        :param payload:
        :return:
        ----------
        """

        # bot/metrio/logs/listeners/reaction.py
        await on_raw_reaction_remove_log(self.bot, payload)


def setup(bot):
    bot.add_cog(OnReaction(bot))
