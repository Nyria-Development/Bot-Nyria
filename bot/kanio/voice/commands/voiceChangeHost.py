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
from typing import Any, Coroutine
from nextcord import PartialInteractionMessage, WebhookMessage
from nextcord.ext import commands
from src.logger.logger import Logging
from src.settings.voice import permissions


class VoiceChangeHost(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(
        name="kanio-voice-change-owner",
        description="Change the owner of your voice channel.",
        force_global=True
    )
    async def change_owner(
            self,
            ctx: nextcord.Interaction,
            user: nextcord.Member
    ) -> PartialInteractionMessage | WebhookMessage | Coroutine[Any, Any, PartialInteractionMessage | WebhookMessage]:

        """
        Attributes
        ----------
        :param ctx:
        :param user:
        :return: None
        ----------
        """

        Logging().info(f"Command :: kanio-voice-change-owner :: {ctx.guild.name} :: {ctx.user}")

        if not await permissions.check(ctx):
            return await ctx.send("You have no permission to do that.", ephemeral=True)

        if ctx.user == user:
            return await ctx.send("You can't banned or unbanned, because you are the owner.", ephemeral=True)

        if ctx.user.voice != user.voice:
            return await ctx.send("The selected user is not in the same voice with you.", ephemeral=True)

        await permissions.change_host(
            channel_id=ctx.user.voice.channel.id,
            member=user
        )
        await ctx.send(f"The voice owner has changed to {user}", ephemeral=True)


def setup(bot):
    bot.add_cog(VoiceChangeHost(bot))
