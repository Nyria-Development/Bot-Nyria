import nextcord
from nextcord.ext import commands
from src.dictionaries import voice


class VoiceRename(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(
        name="kanio-voice-rename",
        description="Rename your voice channel.",
        force_global=True
    )
    async def voice_rename(self, ctx: nextcord.Interaction, voice_channel: nextcord.VoiceChannel, new_name: str):
        if not await voice.check_permissions(ctx=ctx, voice=voice_channel):
            return await ctx.send("You have no permission to do that.", ephemeral=True)

        if len(new_name) > 25:
            return await ctx.send("The new name is to long.", ephemeral=True)

        await voice_channel.edit(name=f"{new_name}-VC")
        await ctx.send(f"The Voice was renamed to **{new_name}-VC**", ephemeral=True)


def setup(bot):
    bot.add_cog(VoiceRename(bot))
