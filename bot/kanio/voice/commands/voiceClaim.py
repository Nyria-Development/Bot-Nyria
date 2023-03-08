import nextcord
from nextcord.ext import commands
from src.dictionarys import voice


class VoiceClaim(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(
        name="kanio-voice-claim",
        description="Claim a talk",
        force_global=True,
        default_member_permissions=8
    )
    async def voice_claim(self, ctx: nextcord.Interaction, voice_channel: nextcord.VoiceChannel):
        category = nextcord.utils.get(ctx.guild.categories, name="--- Nyria Voice ---")
        if category is None:
            return await ctx.send("The voice system is not active", ephemeral=True)

        if voice_channel.name == "Create Voice":
            return await ctx.send("Please select a user channel not a system channel.", ephemeral=True)

        await voice.change_perms(
            user=str(ctx.user),
            voice=voice_channel
        )
        await ctx.send("You have now claimed the channel.", ephemeral=True)


def setup(bot):
    bot.add_cog(VoiceClaim(bot))
