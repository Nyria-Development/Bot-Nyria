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


async def on_raw_reaction_add_log(
        bot,
        payload: nextcord.RawReactionActionEvent
) -> None:
    """
    Attributes
    ----------
    :param bot:
    :param payload:
    :return: None
    ----------
    """

    if payload.member.bot:
        return

    logs = settingLogs.get_logs_on_off(
        guild_id=payload.guild_id
    )
    if logs is False:
        return

    if logs["on_reaction_add"] == "off":
        return

    log_channel = bot.get_channel(logs["log_channel_id"])
    payload_user = bot.get_user(payload.user_id)
    payload_message = await bot.get_channel(payload.channel_id).fetch_message(payload.message_id)
    embed_on_reaction_add = LogEmbed(
        bot=bot,
        user=payload_user,
        title="Reaction | Add",
        description=f"{payload_user.mention} | {payload_message.jump_url}"
    )
    embed_on_reaction_add.add_field(
        name="Reaction",
        value=payload.emoji
    )

    await log_channel.send(embed=embed_on_reaction_add)


async def on_raw_reaction_remove_log(
        bot,
        payload: nextcord.RawReactionActionEvent
) -> None:
    """
    Attributes
    ----------
    :param bot:
    :param payload:
    :return: None
    ----------
    """

    logs = settingLogs.get_logs_on_off(
        guild_id=payload.guild_id
    )

    if logs["on_reaction_remove"] == "off" or not logs:
        return

    log_channel = bot.get_channel(logs["log_channel_id"])
    payload_user = bot.get_user(payload.user_id)
    payload_message = await bot.get_channel(payload.channel_id).fetch_message(payload.message_id)
    embed_on_reaction_remove = LogEmbed(
        bot=bot,
        user=payload_user,
        title="Reaction | Remove",
        description=f"{payload_user.mention} | {payload_message.jump_url}"
    )
    embed_on_reaction_remove.add_field(
        name="Reaction",
        value=payload.emoji
    )

    await log_channel.send(embed=embed_on_reaction_remove)


def setup(bot):
    pass
