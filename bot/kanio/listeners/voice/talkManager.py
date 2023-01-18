import nextcord
from nextcord.ext import commands


class TalkManager(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_voice_state_update(
            self,
            member: nextcord.Member,
            before: nextcord.VoiceState,
            after: nextcord.VoiceState):
        category = nextcord.utils.get(member.guild.categories, name="Voice")

        if str(after.channel) == "Create Voice":
            if len(category.channels) >= 50:
                await member.disconnect()
                return await member.send("There are to many voices. Please try again later.")

            channel = await member.guild.create_voice_channel(name=f"{member.name}-VC", category=category)

            await channel.set_permissions(target=member, priority_speaker=True)
            await member.move_to(channel)

        if str(before.channel) == f"{member.name}-VC":
            channel = nextcord.utils.get(category.channels, name=f"{member.name}-VC")

            await channel.delete()


def setup(bot):
    bot.add_cog(TalkManager(bot))
