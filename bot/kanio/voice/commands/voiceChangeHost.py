import nextcord
from nextcord.ext import commands
from src.dictionaries import voice


class VoiceChangeHost(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(
        name="kanio-voice-change-host",
        description="Change the host.",
        force_global=True
    )
    async def voice_change_host(self, ctx: nextcord.Interaction, voice_channel: nextcord.VoiceChannel, user: nextcord.Member):
        if not await voice.check_permissions(ctx=ctx, voice=voice_channel):
            return await ctx.send("You have no permission to do that.", ephemeral=True)

        await voice.change_perms(
            user=str(user),
            voice=voice_channel
        )
        await ctx.send(f"Host changed to {user}", ephemeral=True)


def setup(bot):
    bot.add_cog(VoiceChangeHost(bot))
