import nextcord
from nextcord.ext import commands
from src.templates import embeds


class NyriaSetup(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(
        name="pyrio-setup",
        description="Setup commands and modules.",
        force_global=True,
        default_member_permissions=8
    )
    async def setup(self, ctx: nextcord.Interaction):
        embed_setup = embeds.TemplateEmbed(
            bot=self.bot,
            ctx=ctx,
            description="Core | Pyrio",
            color=nextcord.Color.brand_green()
        )
        embed_setup.add_field(name="Nyria Setup", value="https://nyria.de/dashboard")
        await ctx.send(embed=embed_setup, ephemeral=True)


def setup(bot):
    bot.add_cog(NyriaSetup(bot))
