import nextcord
from nextcord.ext import commands


class VoiceSetup(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(
        name="pyrio-setup-voice",
        description="Setup your voice system.",
        force_global=True,
        default_member_permissions=8
    )
    async def setup_voice(self, ctx: nextcord.Interaction) -> None:
        category = nextcord.utils.get(ctx.guild.categories, name="--- Nyria Voice ---")

        if category is None:
            category = await ctx.guild.create_category(name="--- Nyria Voice ---")
            await ctx.guild.create_text_channel(
                name="voice-manager",
                category=category
            )
            await ctx.guild.create_voice_channel(
                name="Create Voice",
                category=category
            )

        manager = nextcord.utils.get(category.channels, name="voice-manager")
        if manager is None:
            await ctx.guild.create_text_channel(
                name="voice-manager",
                category=category
            )

        voice = nextcord.utils.get(category.channels, name="Create Voice")
        if voice is None:
            await ctx.guild.create_voice_channel(
                name="Create Voice",
                category=category
            )
        await ctx.send("Voice is ready to use.", ephemeral=True)


def setup(bot):
    bot.add_cog(VoiceSetup(bot))
