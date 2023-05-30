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
from nextcord.ext import commands
from src.logger.logger import Logging
from src.templates.selectors.stringSelect import StringSelect
from src.settings.music import settingQueue


class QueueRemove(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(
        name="diasio-music-queue-remove",
        description="Remove songs from queue",
        guild_ids=[981547050770505819, 1032632067307085955]
    )
    async def queue_remove(
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

        Logging().info(f"Command :: diasio-music-queue-remove :: {ctx.guild.name} :: {ctx.user}")

        current_queue = await settingQueue.get_complete_queue(
            guild_id=ctx.guild.id
        )

        if current_queue is None:
            return await ctx.send("The queue is empty", ephemeral=True)

        selector_queue_remove = StringSelect(
            label_name=current_queue,
            placeholder="Select a track"
        )
        await ctx.send(view=selector_queue_remove)
        await selector_queue_remove.wait()

        track_name = selector_queue_remove.select.values[0]
        await settingQueue.delete_song(
            guild_id=ctx.guild.id,
            song_name=track_name
        )

        await ctx.send(f"Track removed: **{track_name}**")


def setup(bot):
    bot.add_cog(QueueRemove(bot))
