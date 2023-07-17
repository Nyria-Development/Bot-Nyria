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


async def on_guild_channel_create_log(
        bot,
        guild: nextcord.Guild,
        channel: nextcord.abc.GuildChannel
) -> None:
    """
    Attributes
    ----------
    :param channel:
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

    if logs["on_channel_create"] == "off":
        return

    log_channel = logs["log_channel"]

    embed_channel_create = StandAloneEmbed(
        bot=bot,
        color=nextcord.Color.dark_green(),
        description="Channel | Create"
    )
    embed_channel_create.add_field(
        name=f"New {channel.type} - Channel was Created",
        value=channel.jump_url
    )
    await log_channel.send(embed=embed_channel_create)


async def on_guild_channel_delete_log(
        bot,
        guild: nextcord.Guild,
        channel: nextcord.abc.GuildChannel
) -> None:
    """
    Attributes
    ----------
    :param channel:
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

    if logs["on_channel_delete"] == "off":
        return

    log_channel = logs["log_channel"]

    embed_channel_delete = StandAloneEmbed(
        bot=bot,
        color=nextcord.Color.dark_red(),
        description="Channel | Delete"
    )
    embed_channel_delete.add_field(
        name=f"{channel.type} - Channel was deleted",
        value=channel.name
    )
    await log_channel.send(embed=embed_channel_delete)


async def on_guild_channel_update_log(
        bot,
        guild: nextcord.Guild,
        before: nextcord.abc.GuildChannel,
        after: nextcord.abc.GuildChannel
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

    if logs["on_channel_update"] == "off":
        return

    log_channel = logs["log_channel"]

    embed_channel_delete = StandAloneEmbed(
        bot=bot,
        color=nextcord.Color.dark_blue(),
        description="Channel | Update"
    )
    embed_channel_delete.add_field(
        name=f"The Channel {after.jump_url} was updated",
        value=f"{before.name} --> {after.name}"
    )
    await log_channel.send(embed=embed_channel_delete)


def setup(bot):
    pass
