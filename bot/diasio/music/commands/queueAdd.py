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
from src.settings.music import settingQueue
from src.templates.embeds.ctxEmbed import CtxEmbed


class Queue(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(
        name="diasio-music-queue-add",
        description="Add song to the queue",
        guild_ids=[871106346123137054]
    )
    async def queue_add(
            self,
            ctx: nextcord.Interaction,
            track_name: str = nextcord.SlashOption(description="Song name, that you want to add the queue")
    ) -> PartialInteractionMessage | WebhookMessage:

        """
        Attributes
        ----------
        :param ctx:
        :param track_name:
        :return: None
        ----------
        """

        Logging().info(f"Command :: diasio-music-queue-add :: {ctx.guild.name} :: {ctx.user}")

        await ctx.response.defer()

        voice = ctx.user.voice
        node: Node = mafic.NodePool.get_node(guild_id=ctx.guild.id, endpoint="MAIN")
        player = node.get_player(ctx.guild.id)

        if voice is None:
            return await ctx.send("You are not in a voice channel. Please connect.", ephemeral=True)

        if player is None:
            return await ctx.send("The bot doesn't play in the voice channel.", ephemeral=True)

        tracks = await player.fetch_tracks(query=track_name)

        if not tracks:
            return await ctx.send("Track not found")

        await settingQueue.set_song_name(
            ctx=ctx,
            guild_id=ctx.guild.id,
            song_name=track_name
        )

        embed_queue = CtxEmbed(
            bot=self.bot,
            ctx=ctx,
            color=nextcord.Color.orange(),
            description="Fun | Diasio"
        )
        embed_queue.add_field(
            name="Added to queue",
            value=tracks[0].title,
            inline=False
        )
        embed_queue.add_field(
            name="Auther",
            value=tracks[0].author
        )
        embed_queue.add_field(
            name="URL",
            value=tracks[0].uri
        )
        embed_queue.set_thumbnail(
            url=f"https://i.ytimg.com/vi/{tracks[0].identifier}/hq720.jpg"
        )
        await ctx.send(embed=embed_queue)


def setup(bot):
    bot.add_cog(Queue(bot))
    