import nextcord
from nextcord.ext import commands
from src.templates import embeds


class ServerStats(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(
        name="plirio-server-stats",
        description="Show current discord server stats.",
        force_global=True
    )
    async def server_stats(self, ctx: nextcord.Interaction):
        embed_stats = embeds.TemplateEmbed(
            bot=self.bot,
            ctx=ctx,
            description="Information | Plirio",
            color=nextcord.Color.orange()
        )

        server_name = ctx.guild.name
        embed_stats.add_field(name="Server name", value=server_name, inline=False)

        members = len(ctx.guild.members)
        embed_stats.add_field(name="Members", value=members, inline=False)

        server_booster = ctx.guild.premium_subscription_count
        embed_stats.add_field(name="Server booster", value=server_booster, inline=False)

        voice_channels = len(ctx.guild.voice_channels)
        embed_stats.add_field(name="Voice Channels", value=voice_channels, inline=False)

        text_channels = len(ctx.guild.text_channels)
        embed_stats.add_field(name="Text Channels", value=text_channels, inline=False)

        await ctx.send(embed=embed_stats, ephemeral=True)


def setup(bot):
    bot.add_cog(ServerStats(bot))
