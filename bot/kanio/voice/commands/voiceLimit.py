import nextcord
from nextcord.ext import commands
from src.dictionaries import voice


class VoiceLimit(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(
        name="kanio-voice-limit",
        description="Set a limit for your voice channel.",
        force_global=True
    )
    async def voice_limit(self, ctx: nextcord.Interaction, voice_channel: nextcord.VoiceChannel, limit: int):
        if not await voice.check_permissions(ctx=ctx, voice=voice_channel):
            return await ctx.send("You have no permission to do that.", ephemeral=True)

        await voice_channel.edit(user_limit=limit)
        await ctx.send(f"User limit is now by {limit}.", ephemeral=True)


def setup(bot):
    bot.add_cog(VoiceLimit(bot))
