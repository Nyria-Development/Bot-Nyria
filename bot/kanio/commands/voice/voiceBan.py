import nextcord
from nextcord.ext import commands


class VoiceBan(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(
        name="kanio-voice-ban",
        description="Ban any user from your voice channel.",
        force_global=True
    )
    async def voice_ban(self, ctx: nextcord.Interaction, user: nextcord.Member):
        category = nextcord.utils.get(ctx.guild.categories, name="Voice")

        if category is None:
            return await ctx.send("Voices are not furnished.", ephemeral=True)

        # get voice channel
        voice_state = ctx.user.voice
        if voice_state is None:
            return await ctx.send("You are currently not in a voice channel", ephemeral=True)

        if str(ctx.user.name).lower() != str(voice_state.channel.name[:-3]).lower():
            return await ctx.send("You have no permission to do that.", ephemeral=True)

        if user.voice is not None:
            if ctx.user == user:
                return await ctx.send("You can't ban yourself.", ephemeral=True)
            await user.disconnect()

        await voice_state.channel.set_permissions(user, view_channel=False)
        await ctx.send(f"The user {user} was banned from the voice channel.", ephemeral=True)


def setup(bot):
    bot.add_cog(VoiceBan(bot))
