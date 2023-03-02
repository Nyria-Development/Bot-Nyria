from nextcord.ext import commands
import nextcord
import wavelink


class UserInVoice(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_voice_state_update(self, member: nextcord.Member, before: nextcord.VoiceState, after: nextcord.VoiceState):
        try:
            if self.bot.user in before.channel.members and len(before.channel.members) == 1:
                node = wavelink.NodePool.get_node()
                player = node.get_player(member.guild)

                await player.disconnect()
        except AttributeError:
            return


def setup(bot):
    bot.add_cog(UserInVoice(bot))
