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


class Play(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(
        name="diasio-music-play",
        description="Play our favourite song in a voice channel",
        guild_ids=[981547050770505819, 1032632067307085955]
    )
    async def play(
            self,
            ctx: nextcord.Interaction,
            query: str = nextcord.SlashOption(description="Your song name")
    ) -> PartialInteractionMessage | WebhookMessage:

        """
        Attributes
        ----------
        :param ctx:
        :param query:
        :return: None
        ----------
        """

        Logging().info(f"Command :: diasio-music-play :: {ctx.guild.name} :: {ctx.user}")

        await ctx.response.defer()

        voice = ctx.user.voice
        node: Node = mafic.NodePool.get_node(guild_id=ctx.guild.id, endpoint="MAIN")
        player = node.get_player(ctx.guild.id)

        if voice is None:
            return await ctx.send("You are not in a voice channel. Please connect.", ephemeral=True)

        embed_play = CtxEmbed(
            bot=self.bot,
            ctx=ctx,
            color=nextcord.Color.orange(),
            description="Fun | Diasio"
        )

        if player is None:
            player = await ctx.user.voice.channel.connect(cls=mafic.Player)

        if player.connected and player.current is not None:
            tracks = await player.fetch_tracks(query=query)

            if not tracks:
                return await ctx.send("Track not found")

            await settingQueue.set_song_name(
                ctx=ctx,
                guild_id=ctx.guild.id,
                song_name=tracks[0].title
            )
            embed_play.add_field(
                name="Added to queue",
                value=tracks[0].title,
                inline=False
            )
            embed_play.add_field(
                name="Author",
                value=tracks[0].author
            )
            embed_play.add_field(
                name="URL",
                value=tracks[0].uri
            )
            embed_play.set_thumbnail(
                url=f"https://i.ytimg.com/vi/{tracks[0].identifier}/hq720.jpg"
            )
            return await ctx.send(embed=embed_play)

        tracks = await player.fetch_tracks(query=query)

        if not tracks:
            return await ctx.send("Track not found")

        await player.play(tracks[0])

        embed_play.add_field(
            name="Playing",
            value=tracks[0].title,
            inline=False
        )
        embed_play.add_field(
            name="Author",
            value=tracks[0].author
        )
        embed_play.add_field(
            name="URL",
            value=tracks[0].uri
        )
        embed_play.set_thumbnail(
            url=f"https://i.ytimg.com/vi/{tracks[0].identifier}/hq720.jpg"
        )
        await ctx.send(embed=embed_play)


def setup(bot):
    bot.add_cog(Play(bot))
