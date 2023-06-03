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


class OnGuildRole(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_role_create(
            self,
            role: nextcord.Role
    ) -> None:
        """
        Attributes
        ----------
        :param role:
        :return: None
        ----------
        """

        pass

    @commands.Cog.listener()
    async def on_guild_role_delete(
            self,
            role: nextcord.Role
    ) -> None:
        """
        Attributes
        ----------
        :param role:
        :return: None
        ----------
        """

        pass

    @commands.Cog.listener()
    async def on_guild_role_update(
            self,
            before: nextcord.Role,
            after: nextcord.Role
    ) -> None:
        """
        Attributes
        ----------
        :param after:
        :param before:
        :return: None
        ----------
        """

        pass


def setup(bot):
    bot.add_cog(OnGuildRole(bot))
