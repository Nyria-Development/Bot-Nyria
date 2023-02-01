import nextcord
from nextcord.ext import commands
from src.permissions import voice


class VoiceKick(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(
        name="kanio-voice-kick",
        description="Kick any user from your voice channel.",
        force_global=True
    )
    async def voice_kick(self, ctx: nextcord.Interaction, voice_channel: nextcord.VoiceChannel, user: nextcord.Member):
        if not await voice.check_permissions(ctx=ctx, voice=voice_channel):
            return await ctx.send("You have no permission to do that.", ephemeral=True)

        if ctx.user == user:
            return await ctx.send("You can't kick yourself.")

        await user.disconnect()
        await ctx.send(f"You have kicked {user} from the channel.", ephemeral=True)


def setup(bot):
    bot.add_cog(VoiceKick(bot))
