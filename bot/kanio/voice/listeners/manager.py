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
from src.settings.voice import settingVoice, permissions


async def voice_manager(
        bot,
        member: nextcord.Member,
        before: nextcord.VoiceState,
        after: nextcord.VoiceState
) -> None:
    """
    Attributes
    ----------
    :param bot:
    :param member:
    :param before:
    :param after:
    :return: None
    """

    category_name = await settingVoice.get_category(
        guild_id=member.guild.id
    )
    if category_name is None:
        return

    category = nextcord.utils.get(member.guild.categories, name=category_name.lower())

    if str(after.channel) == "Create Voice" and len(category.channels) <= 48:
        channel = await member.guild.create_voice_channel(
            name=f"{member.name}-VC",
            category=category
        )

        await permissions.add_perms(
            channel_id=channel.id,
            member=member
        )

        await member.move_to(channel)

    if before.channel in category.channels and str(before.channel) != "Create Voice" and len(
            before.channel.members) == 0:
        await permissions.remove_perms(
            channel_id=before.channel.id
        )
        empty_channel = bot.get_channel(before.channel.id)
        await empty_channel.delete()


def setup(bot):
    pass
