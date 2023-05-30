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
from src.logger.logger import Logging
from src.templates.embeds.ctxEmbed import CtxEmbed


class Ban(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(
        name="metrio-ban",
        description="Ban user from your server.",
        force_global=True,
        default_member_permissions=8
    )
    async def ban(
            self,
            ctx: nextcord.Interaction,
            user: nextcord.Member = nextcord.SlashOption(
                description="The user you want to ban."
            ),
            reason: str = nextcord.SlashOption(
                description="The reason because you ban the member",
                required=False
            )
    ) -> None:

        """
        Attributes
        ----------
        :param ctx:
        :param user:
        :param reason:
        :return: None
        ----------
        """

        Logging().info(f"Command :: metrio-ban :: {ctx.guild.name} :: {ctx.user}")

        await ctx.guild.ban(
            user=user,
            reason=reason
        )

        embed_ban = CtxEmbed(
            bot=self.bot,
            ctx=ctx,
            color=nextcord.Color.red(),
            description="Metrio | Moderation"
        )
        embed_ban.add_field(
            name=f"Banned from {ctx.guild}",
            value=reason
        )
        await ctx.send(embed=embed_ban, ephemeral=True)


def setup(bot):
    bot.add_cog(Ban(bot))
