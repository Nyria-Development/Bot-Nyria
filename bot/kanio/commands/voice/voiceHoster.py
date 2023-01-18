import nextcord
from nextcord.ext import commands


class VoiceHost(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(
        name="kanio-voice-change-host",
        description="Change the Host of the voice channel.",
        force_global=True
    )
    async def voice_change_host(self, ctx: nextcord.Interaction, user: nextcord.Member):
        category = nextcord.utils.get(ctx.guild.categories, name="Voice")

        if category is None:
            return await ctx.send("Voices are not furnished.", ephemeral=True)

        # get voice channel
        voice_state = ctx.user.voice

        if str(ctx.user.name).lower() != str(voice_state.channel.name[:-3]).lower():
            return await ctx.send("You have no permission to do that.", ephemeral=True)

        await voice_state.channel.edit(name=f"{user.name}-VC")
        await ctx.send(f"Host changed to {user}")


def setup(bot):
    bot.add_cog(VoiceHost(bot))
