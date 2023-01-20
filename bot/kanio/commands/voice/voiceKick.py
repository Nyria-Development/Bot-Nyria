import nextcord
from nextcord.ext import commands


class VoiceKick(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(
        name="kanio-voice-kick",
        description="Kick any user from the voice channel.",
        force_global=True
    )
    async def voice_kick(self, ctx: nextcord.Interaction, user: nextcord.Member):
        category = nextcord.utils.get(ctx.guild.categories, name="Voice")

        if category is None:
            return await ctx.send("Voices are not furnished.", ephemeral=True)

        # get voice channel
        voice_state = ctx.user.voice
        if voice_state is None or user.voice is None:
            return await ctx.send("Someone of you is not in the voice channel", ephemeral=True)

        if str(ctx.user.name).lower() != str(voice_state.channel.name[:-3]).lower():
            return await ctx.send("You have no permission to do that.", ephemeral=True)

        if ctx.user == user:
            return await ctx.send("You can't kick yourself.", ephemeral=True)

        await user.disconnect()
        await ctx.send(f"The user {user} was kicked from the voice channel.", ephemeral=True)


def setup(bot):
    bot.add_cog(VoiceKick(bot))
