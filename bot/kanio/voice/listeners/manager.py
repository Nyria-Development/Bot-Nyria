import nextcord
from nextcord.ext import commands
from src.permissions import voice


class VoiceManager(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_voice_state_update(self, member: nextcord.Member, before: nextcord.VoiceState,
                                    after: nextcord.VoiceState):
        category = nextcord.utils.get(member.guild.categories, name="--- Nyria Voice ---")

        if category is None:
            return

        if category is not None and str(after.channel) == "Create Voice" and len(category.channels) <= 48:
            channel = await member.guild.create_voice_channel(name=f"{member.name}-VC", category=category)

            # setup perms
            await voice.add_perms(
                channel_id=channel.id,
                member=member
            )
            await member.move_to(channel=channel)

        if before.channel in category.channels and str(before.channel) != "Create Voice" and len(before.channel.members) == 0:
            await voice.remove_perms(before.channel.id)
            channel = self.bot.get_channel(before.channel.id)
            await channel.delete()


def setup(bot):
    bot.add_cog(VoiceManager(bot))
