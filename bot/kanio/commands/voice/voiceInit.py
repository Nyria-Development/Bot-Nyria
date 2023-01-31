import nextcord
from nextcord.ext import commands


class VoiceInit(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(
        name="kanio-voice-init",
        description="Setup for voice system.",
        force_global=True,
        default_member_permissions=8
    )
    async def voice_init(self, ctx: nextcord.Interaction):
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
    bot.add_cog(VoiceInit(bot))
