import nextcord
from nextcord.ext import commands
from src.templates import embeds
from src.loader.jsonLoader import Plirio


class Credits(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(
        name="plirio-credits",
        description="Thanks for your support!",
        force_global=True
    )
    async def credits(self, ctx: nextcord.Interaction):
        config = Plirio().credits()
        embed_credits = embeds.TemplateEmbed(
            bot=self.bot,
            ctx=ctx,
            description="Information | Plirio",
            color=nextcord.Color.orange()
        )
        embed_credits.add_field(name="Artworks | AbiSilver#1257", value=config["credits"]["abi"])
        await ctx.send(embed=embed_credits, ephemeral=True)


def setup(bot):
    bot.add_cog(Credits(bot))
