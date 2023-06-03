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

from bot.metrio.logs.listeners.moderation import on_member_ban_log, on_member_unban_log


class OnMember(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member: nextcord.Member) -> None:
        """
        Attributes
        ----------
        :param member:
        :return: None
        ----------
        """

        pass

    @commands.Cog.listener()
    async def on_member_remove(self, member: nextcord.Member) -> None:
        """
        Attributes
        ----------
        :param member:
        :return: None
        ----------
        """

        pass

    @commands.Cog.listener()
    async def on_member_ban(self, guild: nextcord.Guild, user: nextcord.Member) -> None:
        """
        Attributes
        ----------
        :param user:
        :param guild:
        :return: None
        ----------
        """

        # bot/metrio/logs/listeners/moderation.py
        await on_member_ban_log(self.bot, guild, user)

    @commands.Cog.listener()
    async def on_member_unban(self, guild: nextcord.Guild, user: nextcord.Member) -> None:
        """
        Attributes
        ----------
        :param user:
        :param guild:
        :return: None
        ----------
        """

        # bot/metrio/logs/listeners/moderation.py
        await on_member_unban_log(self.bot, guild, user)

    @commands.Cog.listener()
    async def on_member_update(self, before: nextcord.Member, after: nextcord.Member) -> None:
        """
        Attributes
        ----------
        :param after:
        :param before:
        :return: None
        ----------
        """

        pass


def setup(bot):
    bot.add_cog(OnMember(bot))
