import nextcord
import random
from nextcord import PartialInteractionMessage, WebhookMessage
from nextcord.ext import commands
from src.templates.embeds.ctxEmbed import CtxEmbed
from src.logger.logger import Logging


class Dice(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(
        name="diasio-dice",
        description="Generate a random number.",
        force_global=True
    )
    async def dice(
            self,
            ctx: nextcord.Interaction,
            first_number: int = nextcord.SlashOption(description="The first number. Starts here"),
            second_number: int = nextcord.SlashOption(description="The second number. Ends here")
    ) -> PartialInteractionMessage | WebhookMessage:

        """
        Attributes
        ----------
        :param ctx:
        :param first_number:
        :param second_number:
        :return: PartialInteractionMessage | WebhookMessage
        ----------
        """

        Logging().info(f"Command :: diasio-dice :: {ctx.guild.name} :: {ctx.user}")

        if first_number >= second_number:
            return await ctx.send("The second number must be higher than the first number.", ephemeral=True)

        ran_num = random.randint(first_number, second_number)

        embed_random_number = CtxEmbed(
            bot=self.bot,
            ctx=ctx,
            description="Fun | Diasio",
            color=nextcord.Color.orange()
        )
        embed_random_number.add_field(
            name="Random number",
            value=ran_num
        )
        await ctx.send(embed=embed_random_number, ephemeral=True)


def setup(bot):
    bot.add_cog(Dice(bot))
