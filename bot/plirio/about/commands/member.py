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
from src.loader.credits import GetCredits
from src.logger.logger import Logging
from src.templates.embeds.ctxEmbed import CtxEmbed


class MemberInfo(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(
        name="plirio-member-info",
        description="Information of a member!",
        force_global=True
    )
    async def credits(
            self,
            ctx: nextcord.Interaction,
            member: nextcord.Member
    ) -> None:
        """
        Attributes
        ----------
        :param member:
        :param ctx:
        :return: None
        ----------
        """

        Logging().info(f"Command :: plirio-member-info :: {ctx.guild.name} :: {ctx.user}")

        embed_member_info = CtxEmbed(
            bot=self.bot,
            ctx=ctx,
            description="Information | Member",
            color=member.color
        )
        embed_member_info.set_thumbnail(url=member.avatar)
        embed_member_info.set_author(name=member.name, icon_url=member.avatar)
        embed_member_info.add_field(
            name="User",
            value=member.mention,
        )
        embed_member_info.add_field(
            name="Name",
            value=member.name,
        )
        embed_member_info.add_field(
            name="Status",
            value=member.status,
        )
        embed_member_info.add_field(
            name="Roles",
            value="".join(f"{role.mention}, " for role in member.roles),
        )
        await ctx.send(embed=embed_member_info, ephemeral=True)


def setup(bot):
    bot.add_cog(MemberInfo(bot))
