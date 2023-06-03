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
from src.templates.embeds.logEmbed import LogEmbed


async def on_message_log(
        bot,
        message: nextcord.Message
) -> None:
    """
    Attributes
    ----------
    :param bot:
    :param message:
    :return: None
    ----------
    """

    if message.author.bot:
        return

    logs = settingLogs.get_logs_on_off(
        guild_id=message.guild.id
    )

    if not logs or logs["on_message"] == "off":
        return

    log_channel = bot.get_channel(logs["log_channel_id"])
    embed_on_message = LogEmbed(
        bot=bot,
        user=message.author,
        title="Message | NewMessage",
        description=f"{message.author.mention} | {message.jump_url}"
    )

    if message.content:
        embed_on_message.add_field(
            name="Content",
            value=message.content
        )
    if message.attachments:
        embed_on_message.add_field(
            name="Attachments",
            value=message.attachments
        )
    await log_channel.send(embed=embed_on_message)


async def on_message_edit_log(
        bot,
        before: nextcord.Message,
        after: nextcord.Message
) -> None:
    """
    Attributes
    ----------
    :param bot:
    :param before
    :param after
    :return: None
    ----------
    """

    if before.author.bot:
        return

    logs = settingLogs.get_logs_on_off(
        guild_id=before.guild.id
    )
    if logs is False:
        return

    if logs["on_message_edit"] == "off":
        return

    log_channel = bot.get_channel(logs["log_channel_id"])
    embed_on_message = LogEmbed(
        bot=bot,
        user=after.author,
        title="Message | MessageEdit",
        description=f"{after.author.mention} | {after.jump_url}"
    )

    if before.content:
        embed_on_message.add_field(
            name="Content before",
            value=before.content,
            inline=False
        )
        embed_on_message.add_field(
            name="Content after",
            value=after.content
        )
    await log_channel.send(embed=embed_on_message)


async def on_message_delete_log(
        bot,
        message: nextcord.Message
) -> None:
    """
    Attributes
    ----------
    :param bot:
    :param message:
    :return: None
    ----------
    """

    if message.author.bot:
        return

    logs = settingLogs.get_logs_on_off(
        guild_id=message.guild.id
    )
    if logs is False:
        return

    if logs["on_message_delete"] == "off":
        return

    log_channel = bot.get_channel(logs["log_channel_id"])
    embed_on_message = LogEmbed(
        bot=bot,
        user=message.author,
        title="Message | MessageEdit",
        description=f"{message.author.mention} | {message.jump_url}"
    )

    if message.content:
        embed_on_message.add_field(
            name="Message deleted",
            value=message.content
        )
    await log_channel.send(embed=embed_on_message)


def setup(bot):
    pass
