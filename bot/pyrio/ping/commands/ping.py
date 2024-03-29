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
from src.templates.embeds.ctxEmbed import CtxEmbed
from src.logger.logger import Logging


class Ping(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(
        name="pyrio-ping",
        description="Show the ping from the bot.",
        force_global=True
    )
    async def ping(
            self,
            ctx: nextcord.Interaction
    ) -> None:

        """
        Attributes
        ----------
        :param ctx:
        :return: None
        ----------
        """

        Logging().info(f"Command :: pyrio-ping :: {ctx.guild.name} :: {ctx.user}")

        embed_ping = CtxEmbed(
            bot=self.bot,
            ctx=ctx,
            color=nextcord.Color.brand_green(),
            description="Core | Pyrio"
        )
        embed_ping.add_field(
            name="Nyria's ping",
            value=f"**{round(self.bot.latency * 100)}ms**"
        )
        await ctx.send(embed=embed_ping, ephemeral=True)


def setup(bot):
    bot.add_cog(Ping(bot))
