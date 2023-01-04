import nextcord
from nextcord.ext import commands
from templates import embeds


class Ping(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(
        name="pyrio-ping",
        description="Show the ping from the bot.",
        force_global=True
    )
    async def ping(self, ctx: nextcord.Interaction):
        embed_ping = embeds.TemplateEmbed(
            bot=self.bot,
            ctx=ctx,
            color=nextcord.Color.brand_green(),
            description="Core | Pyrio"
        )
        embed_ping.add_field(
            name="--> Ping <--",
            value=f"The ping is by: **{round(self.bot.latency * 100)}ms**"
        )
        await ctx.send(embed=embed_ping, ephemeral=True)


def setup(bot):
    bot.add_cog(Ping(bot))
