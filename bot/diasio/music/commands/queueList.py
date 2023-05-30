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
from src.templates.embeds.ctxEmbed import CtxEmbed
from src.settings.music import settingQueue


class QueueList(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(
        name="diasio-music-queue-list",
        description="List the queue's songs.",
        guild_ids=[981547050770505819, 1032632067307085955]
    )
    async def queue_list(
            self,
            ctx: nextcord.Interaction
    ) -> PartialInteractionMessage | WebhookMessage:

        """
        Attributes
        ----------
        :param ctx: The discord interaction
        :return: None
        ----------
        """

        Logging().info(f"Command :: diasio-music-queue-list :: {ctx.guild.name} :: {ctx.user}")

        current_queue = await settingQueue.get_complete_queue(
            guild_id=ctx.guild.id
        )

        if current_queue is None:
            return await ctx.send("Your queue is empty", ephemeral=True)

        embed_list_queue = CtxEmbed(
            bot=self.bot,
            ctx=ctx,
            color=nextcord.Color.orange(),
            description="Fun | Diasio"
        )
        embed_list_queue.add_field(
            name="Queue",
            value="\n".join(current_queue)
        )
        await ctx.send(embed=embed_list_queue)


def setup(bot):
    bot.add_cog(QueueList(bot))
