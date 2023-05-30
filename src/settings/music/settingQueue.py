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
from nextcord import PartialInteractionMessage, WebhookMessage

__queue = {}


async def set_song_name(
        ctx: nextcord.Interaction,
        guild_id: int,
        song_name: str
) -> None | PartialInteractionMessage | WebhookMessage:

    """
    Attributes
    ----------
    :param ctx:
    :param guild_id:
    :param song_name:
    :return: None | PartialInteractionMessage | WebhookMessage
    ----------
    """

    if guild_id not in __queue:
        __queue[guild_id] = [song_name.lower()]
        return

    if len(__queue[guild_id]) >= 25:
        return await ctx.send("Queue is full. Please delete songs to add new songs.", ephemeral=True)

    if song_name.lower() in __queue[guild_id]:
        return await ctx.send("This song is currently in the queue.", ephemeral=True)

    __queue[guild_id].append(song_name.lower())


async def get_song_name(
        guild_id: int
) -> str | None:

    """
    Attributes
    ----------
    :param guild_id:
    :return: str
    ----------
    """

    if len(__queue[guild_id]) == 0:
        return

    song = __queue[guild_id][-1]
    __queue[guild_id].pop()

    return song


async def get_complete_queue(
        guild_id: int
) -> None | list:

    """
    Attributes
    ----------
    :param guild_id:
    :return: list
    ----------
    """

    try:
        queue = __queue[guild_id]
    except KeyError:
        return

    return queue


async def delete_song(
        guild_id: int,
        song_name: str
) -> None:

    """
    Attributes
    ----------
    :param guild_id:
    :param song_name:
    :return: None
    ----------
    """

    __queue[guild_id].remove(song_name)
