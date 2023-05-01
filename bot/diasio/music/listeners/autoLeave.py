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
