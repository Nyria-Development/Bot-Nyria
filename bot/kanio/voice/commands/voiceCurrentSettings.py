import nextcord
from nextcord.ext import commands
from src.templates import embeds
from src.dictionarys import voice


class VoiceCurrentSettings(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(
        name="kanio-voice-current-settings",
        description="Show the current voice settings.",
        force_global=True
    )
    async def voice_current_settings(self, ctx: nextcord.Interaction, voice_channel: nextcord.VoiceChannel):
        category = nextcord.utils.get(ctx.guild.categories, name="--- Nyria Voice ---")
        if category is None:
            return await ctx.send("The voice system is not active", ephemeral=True)

        if voice_channel.name == "Create Voice":
            return await ctx.send("Please select a user channel not a system channel.", ephemeral=True)

        if voice_channel not in category.channels:
            return await ctx.send(f"Please select a channel in **{category.name}**", ephemeral=True)

        host = await voice.get_host(voice_channel.id)
        embed_settings = embeds.TemplateEmbed(
            bot=self.bot,
            ctx=ctx,
            description="Channel | Kanio",
            color=nextcord.Color.blurple()
        )
        embed_settings.add_field(name="Host", value=host["voice_owner"], inline=False)
        embed_settings.add_field(name="Aktive Users", value=len(voice_channel.members))
        embed_settings.add_field(name="Limit", value=voice_channel.user_limit)

        await ctx.send(embed=embed_settings, ephemeral=True)


def setup(bot):
    bot.add_cog(VoiceCurrentSettings(bot))
