import nextcord
from nextcord.ext import commands


class VoiceUnban(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(
        name="kanio-voice-unban",
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

        await voice_state.channel.set_permissions(user, view_channel=True)
        await ctx.send(f"The user {user} was unbanned.", ephemeral=True)


def setup(bot):
    bot.add_cog(VoiceUnban(bot))
