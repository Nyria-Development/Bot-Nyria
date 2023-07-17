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
from src.settings.logs import settingLogs
from src.templates.embeds.standAloneEmbed import StandAloneEmbed


async def on_member_ban_log(
        bot,
        guild: nextcord.Guild,
        user: nextcord.Member
) -> None:
    """
    Attributes
    ----------
    :param bot:
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

    if logs["on_member_ban"] == "off":
        return

    log_channel = logs["log_channel"]

    embed_member_ban = StandAloneEmbed(
        bot=bot,
        color=nextcord.Color.red(),
        description="Moderation | Ban"
    )
    embed_member_ban.add_field(
        name="User banned",
        value=str(user)
    )
    await log_channel.send(embed=embed_member_ban)


async def on_member_unban_log(
        bot,
        guild: nextcord.Guild,
        user: nextcord.Member
) -> None:
    """
    Attributes
    ----------
    :param bot:
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

    if logs["on_member_unban"] == "off":
        return

    log_channel = logs["log_channel"]

    embed_member_unban = StandAloneEmbed(
        bot=bot,
        color=nextcord.Color.red(),
        description="Moderation | Unban"
    )
    embed_member_unban.add_field(
        name="User unbanned",
        value=str(user)
    )
    await log_channel.send(embed=embed_member_unban)


async def on_member_join_log(
        bot,
        guild: nextcord.Guild,
        member: nextcord.Member
) -> None:
    """
    Attributes
    ----------
    :param member:
    :param bot:
    :param guild:
    :return: None
    ----------
    """

    logs = settingLogs.get_logs_on_off(
        guild_id=guild.id
    )
    if logs is False:
        return

    if logs["on_member_join"] == "off":
        return

    log_channel = logs["log_channel"]

    embed_member_join = StandAloneEmbed(
        bot=bot,
        color=nextcord.Color.green(),
        description="Moderation | Member Join"
    )
    embed_member_join.add_field(
        name="User joined the Discord",
        value=member.mention
    )
    await log_channel.send(embed=embed_member_join)


async def on_member_remove_log(
        bot,
        guild: nextcord.Guild,
        member: nextcord.Member
) -> None:
    """
    Attributes
    ----------
    :param member:
    :param bot:
    :param guild:
    :return: None
    ----------
    """

    logs = settingLogs.get_logs_on_off(
        guild_id=guild.id
    )
    if logs is False:
        return

    if logs["on_member_remove"] == "off":
        return

    log_channel = logs["log_channel"]

    embed_member_remove = StandAloneEmbed(
        bot=bot,
        color=nextcord.Color.green(),
        description="Moderation | Member Remove"
    )
    embed_member_remove.add_field(
        name="User left the Discord",
        value=str(member)
    )
    await log_channel.send(embed=embed_member_remove)


async def on_member_update_nick_log(
        bot,
        guild: nextcord.Guild,
        before: nextcord.Member,
        after: nextcord.Member
) -> None:
    """
    Attributes
    ----------
    :param after:
    :param before:
    :param bot:
    :param guild:
    :return: None
    ----------
    """

    logs = settingLogs.get_logs_on_off(
        guild_id=guild.id
    )
    if logs is False:
        return

    if logs["on_member_update_nick"] == "off":
        return

    log_channel = logs["log_channel"]

    embed_member_update_nick = StandAloneEmbed(
        bot=bot,
        color=nextcord.Color.dark_blue(),
        description="Moderation | Member Nick"
    )
    embed_member_update_nick.add_field(
        name="User changed his nick",
        value=after.mention,
        inline=False
    )
    embed_member_update_nick.add_field(
        name="User Nick before",
        value=before.nick
    )
    embed_member_update_nick.add_field(
        name="User Nick after",
        value=after.nick
    )
    await log_channel.send(embed=embed_member_update_nick)


async def on_member_update_avatar_log(
        bot,
        guild: nextcord.Guild,
        before: nextcord.Member,
        after: nextcord.Member
) -> None:
    """
    Attributes
    ----------
    :param after:
    :param before:
    :param bot:
    :param guild:
    :return: None
    ----------
    """

    logs = settingLogs.get_logs_on_off(
        guild_id=guild.id
    )
    if logs is False:
        return

    if logs["on_member_update_nick"] == "off":
        return

    log_channel = logs["log_channel"]

    embed_member_update_avatar = StandAloneEmbed(
        bot=bot,
        color=nextcord.Color.dark_blue(),
        description="Moderation | Member Avatar"
    )
    embed_member_update_avatar.add_field(
        name="User changed his Avatar",
        value=after.mention,
        inline=False
    )
    embed_member_update_avatar.add_field(
        name="User Nick before",
        value=before.avatar
    )
    embed_member_update_avatar.add_field(
        name="User Nick after",
        value=after.avatar
    )
    await log_channel.send(embed=embed_member_update_avatar)


def setup(bot):
    pass
