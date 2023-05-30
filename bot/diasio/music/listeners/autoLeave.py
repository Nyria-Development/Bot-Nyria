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
from nextcord.ext import commands


class AutoLeave(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_voice_state_update(
            self,
            member: nextcord.Member,
            before: nextcord.VoiceState,
            after: nextcord.VoiceState
    ) -> None:

        """
        Attributes
        ----------
        :param member:
        :param before:
        :param after:
        :return: None
        ----------
        """

        if before.channel is None and after.channel is not None:
            return

        node: Node = mafic.NodePool.get_node(guild_id=member.guild.id, endpoint="MAIN")
        player = node.get_player(member.guild.id)

        if player is None:
            return

        if player.is_connected():
            await player.destroy()


def setup(bot):
    bot.add_cog(AutoLeave(bot))
