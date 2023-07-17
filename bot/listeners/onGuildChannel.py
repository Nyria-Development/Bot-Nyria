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

from bot.metrio.logs.listeners.channels import on_guild_channel_create_log, on_guild_channel_delete_log, \
    on_guild_channel_update_log


class OnGuildChannel(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_channel_create(
            self,
            channel: nextcord.abc.GuildChannel
    ) -> None:
        """
        Attributes
        ----------
        :param channel:
        :return: None
        ----------
        """

        # bot/metrio/logs/listeners/channels.py
        await on_guild_channel_create_log(bot=self.bot, guild=channel.guild, channel=channel)

    @commands.Cog.listener()
    async def on_guild_channel_delete(
            self,
            channel: nextcord.abc.GuildChannel
    ) -> None:
        """
        Attributes
        ----------
        :param channel:
        :return: None
        ----------
        """

        # bot/metrio/logs/listeners/channels.py
        await on_guild_channel_delete_log(bot=self.bot, guild=channel.guild, channel=channel)

    @commands.Cog.listener()
    async def on_guild_channel_update(
            self,
            before: nextcord.abc.GuildChannel,
            after: nextcord.abc.GuildChannel
    ) -> None:
        """
        Attributes
        ----------
        :param after:
        :param before:
        :return: None
        ----------
        """

        print(before, after)
        print(before.name, after.name)

        # bot/metrio/logs/listeners/channels.py
        await on_guild_channel_update_log(bot=self.bot, guild=after.guild, before=before, after=after)


def setup(bot):
    bot.add_cog(OnGuildChannel(bot))
