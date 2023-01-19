import nextcord
from nextcord.ext import commands
from templates import embeds


class VoiceCurrentSettings(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(
        name="kanio-voice-current-settings",
        description="See the current settings of the voice channel",
        force_global=True
    )
    async def voice_current_settings(self, ctx: nextcord.Interaction):
        category = nextcord.utils.get(ctx.guild.categories, name="Voice")

        if category is None:
            return await ctx.send("Voices are not furnished.", ephemeral=True)

        # get voice channel
        voice_state = ctx.user.voice
        if voice_state is None:
            return await ctx.send("You are currently not in a voice channel.", ephemeral=True)

        if voice_state.channel not in category.channels:
            return await ctx.send("You are not in voice by nyria.", ephemeral=True)

        embed_current_settings = embeds.TemplateEmbed(
            bot=self.bot,
            ctx=ctx,
            description="Channels | Kanio",
            color=nextcord.Color.blurple()
        )
        embed_current_settings.add_field(name="Voice Host", value=ctx.user, inline=False)
        embed_current_settings.add_field(name="User Limit", value=voice_state.channel.user_limit)
        embed_current_settings.add_field(name="Channel ID", value=voice_state.channel.id)
        embed_current_settings.add_field(name="Muted", value=voice_state.self_mute, inline=False)

        await ctx.send(embed=embed_current_settings, ephemeral=True)


def setup(bot):
    bot.add_cog(VoiceCurrentSettings(bot))
