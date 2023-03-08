import nextcord
from nextcord.ext import commands
from src.dictionarys import voice


class VoiceUnban(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(
        name="kanio-voice-unban",
        description="Ban any user from your voice channel.",
        force_global=True
    )
    async def voice_unban(self, ctx: nextcord.Interaction, voice_channel: nextcord.VoiceChannel, user: nextcord.Member):
        if not await voice.check_permissions(ctx=ctx, voice=voice_channel):
            return await ctx.send("You have no permission to do that.", ephemeral=True)

        await voice_channel.set_permissions(user, view_channel=True)
        await ctx.send(f"You have unbanned {user} from the channel.", ephemeral=True)


def setup(bot):
    bot.add_cog(VoiceUnban(bot))