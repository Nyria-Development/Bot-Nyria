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
import mafic
from mafic import Node
from nextcord import PartialInteractionMessage, WebhookMessage
from nextcord.ext import commands
from src.logger.logger import Logging


class Pause(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(
        name="diasio-music-pause",
        description="Pause the song in voice channel.",
        guild_ids=[871106346123137054]
    )
    async def pause(
            self,
            ctx: nextcord.Interaction
    ) -> PartialInteractionMessage | WebhookMessage:

        """
        Attributes
        ----------
        :param ctx:
        :return: None
        ----------
        """

        Logging().info(f"Command :: diasio-music-pause :: {ctx.guild.name} :: {ctx.user}")

        voice = ctx.user.voice
        node: Node = mafic.NodePool.get_node(guild_id=ctx.guild.id, endpoint="MAIN")
        player = node.get_player(ctx.guild.id)

        if voice is None:
            return await ctx.send("You are not in a voice channel. Please connect.", ephemeral=True)

        if player is None:
            return await ctx.send("The bot doesn't play in the voice channel.", ephemeral=True)

        if player.paused:
            return await ctx.send("The bot is already paused.", ephemeral=True)

        await player.pause()
        await ctx.send("Music paused")


def setup(bot):
    bot.add_cog(Pause(bot))
