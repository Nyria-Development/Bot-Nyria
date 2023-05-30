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
from src.settings.logs import settingLogs
from src.templates.embeds.standAloneEmbed import StandAloneEmbed


class LogModeration(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_ban(
            self,
            guild: nextcord.Guild,
            user: nextcord.Member
    ) -> None:

        """
        Attributes
        ----------
        :param guild:
        :param user:
        :return: None
        ----------
        """

        logs = settingLogs.get_logs_on_off(
            guild_id=guild.id
        )
        if logs is False:
            return

        if logs["on_message"] == "off":
            return

        log_channel = self.bot.get_channel(logs["log_channel_id"])

        embed_member_ban = StandAloneEmbed(
            bot=self.bot,
            color=nextcord.Color.red(),
            description="Metrio | Moderation"
        )
        embed_member_ban.add_field(
            name="User banned",
            value=str(user)
        )
        await log_channel.send(embed=embed_member_ban)

    @commands.Cog.listener()
    async def on_member_unban(
            self,
            guild: nextcord.Guild,
            user: nextcord.Member
    ) -> None:

        """
        Attributes
        ----------
        :param guild:
        :param user:
        :return: None
        ----------
        """

        logs = settingLogs.get_logs_on_off(
            guild_id=guild.id
        )
        if logs is False:
            return

        if logs["on_message"] == "off":
            return

        log_channel = self.bot.get_channel(logs["log_channel_id"])

        embed_member_unban = StandAloneEmbed(
            bot=self.bot,
            color=nextcord.Color.red(),
            description="Metrio | Moderation"
        )
        embed_member_unban.add_field(
            name="User unbanned",
            value=str(user)
        )
        await log_channel.send(embed=embed_member_unban)


def setup(bot):
    bot.add_cog(LogModeration(bot))
