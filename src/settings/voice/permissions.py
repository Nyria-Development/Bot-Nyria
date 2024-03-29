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

__perms = dict()


async def add_perms(
        channel_id: int,
        member: nextcord.Member
) -> None:

    """
    Attributes
    ----------
    :param channel_id:
    :param member:
    :return: None
    ----------
    """

    __perms[channel_id] = {"voice_owner": str(member)}


async def remove_perms(
        channel_id: int
) -> None:

    """
    Attributes
    ----------
    :param channel_id:
    :return: None
    ----------
    """

    del __perms[channel_id]


async def check(
        ctx: nextcord.Interaction
) -> bool:

    """
    Attributes
    ----------
    :param ctx:
    :return: bool
    ----------
    """

    voice = ctx.user.voice
    if voice is None:
        return False

    if voice.channel.id in __perms:
        if __perms[voice.channel.id]["voice_owner"] == str(ctx.user):
            return True

    return False


async def change_host(
        channel_id: int,
        member: nextcord.Member
) -> None:

    """
    Attributes
    ----------
    :param channel_id:
    :param member:
    :return: None
    ----------
    """

    __perms[channel_id]["voice_owner"] = str(member)


async def get_host(
        channel_id: int
) -> str:

    """
    Attributes
    ----------
    :param channel_id:
    :return: str
    ----------
    """

    return __perms[channel_id]["voice_owner"]
