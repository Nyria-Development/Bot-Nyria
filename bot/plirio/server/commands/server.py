import nextcord
from nextcord.ext import commands
from src.logger.logger import Logging
from src.templates.embeds.ctxEmbed import CtxEmbed


class ServerStats(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(
        name="plirio-server-stats",
        description="Show the current discord server stats.",
        force_global=True
    )
    async def server_stats(
            self,
            ctx: nextcord.Interaction
    ) -> None:

        """
        Attributes
        ----------
        :param ctx:
        :return: None
        ----------
        """

        Logging().info(f"Command :: plirio-server-stats :: {ctx.guild.name} :: {ctx.user}")

        embed_server_stats = CtxEmbed(
            bot=self.bot,
            ctx=ctx,
            description="Information | Plirio",
            color=nextcord.Color.orange()
        )

        embed_server_stats.set_thumbnail(
            url=ctx.guild.icon
        )

        server_name = ctx.guild.name
        embed_server_stats.add_field(
            name="Server name",
            value=server_name
        )

        guild_description = ctx.guild.description
        embed_server_stats.add_field(
            name="Server description",
            value=guild_description
        )

        guild_created = ctx.guild.created_at.strftime(f"Date: %d/%m/%Y | Time: %H:%M:%S")
        embed_server_stats.add_field(
            name="Created",
            value=guild_created,
            inline=False
        )

        guild_members = ctx.guild.member_count
        embed_server_stats.add_field(
            name="Members",
            value=guild_members
        )

        guild_bots = len(ctx.guild.bots)
        embed_server_stats.add_field(
            name="Bots",
            value=guild_bots,
        )

        server_booster = ctx.guild.premium_subscription_count
        embed_server_stats.add_field(
            name="Server booster",
            value=server_booster
        )

        voice_channels = len(ctx.guild.voice_channels)
        embed_server_stats.add_field(
            name="All voice channels",
            value=voice_channels
        )

        text_channels = len(ctx.guild.text_channels)
        embed_server_stats.add_field(
            name="All text channels",
            value=text_channels
        )
        await ctx.send(embed=embed_server_stats, ephemeral=True)


def setup(bot):
    bot.add_cog(ServerStats(bot))
