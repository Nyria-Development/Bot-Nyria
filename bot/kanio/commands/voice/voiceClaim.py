import nextcord
from nextcord.ext import commands


class VoiceClaim(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(
        name="kanio-voice-claim",
        description="Claim a channel to moderate.",
        force_global=True,
        default_member_permissions=8
    )
    async def voice_claim(self, ctx: nextcord.Interaction, channel: nextcord.VoiceChannel):
        category = nextcord.utils.get(ctx.guild.categories, name="Voice")

        if category is None:
            return await ctx.send("Voices are not furnished.", ephemeral=True)

        if channel not in category.channels:
            return await ctx.send(f"This voice is not in category **{category.name}**", ephemeral=True)

        await channel.edit(name=f"{ctx.user.name}-VC")
        await ctx.send("Channel claimed.", ephemeral=True)


def setup(bot):
    bot.add_cog(VoiceClaim(bot))
