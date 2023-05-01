import nextcord
from nextcord.ext import commands
from src.loader.credits import GetCredits
from src.logger.logger import Logging
from src.templates.embeds.ctxEmbed import CtxEmbed


class Credits(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(
        name="plirio-credits",
        description="Thanks for your support!",
        force_global=True
    )
    async def credits(
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

        Logging().info(f"Command :: plirio-credits :: {ctx.guild.name} :: {ctx.user}")

        config = GetCredits().get_credits()
        embed_credits = CtxEmbed(
            bot=self.bot,
            ctx=ctx,
            description="Information | Plirio",
            color=nextcord.Color.orange()
        )
        embed_credits.add_field(
            name="Artworks | AbiSilver#1257",
            value=config["abi_silver"],
            inline=False
        )
        embed_credits.add_field(
            name="Developer | meLordlp#3140",
            value=config["meLordlp"],
            inline=False
        )
        embed_credits.add_field(
            name="Co-Founder | wetter_lachs#0414",
            value=config["wetter_lachs"],
            inline=False
        )
        embed_credits.add_field(
            name="Founder | Redtronics#4794",
            value=config["redtronics"],
            inline=False
        )
        await ctx.send(embed=embed_credits, ephemeral=True)


def setup(bot):
    bot.add_cog(Credits(bot))
