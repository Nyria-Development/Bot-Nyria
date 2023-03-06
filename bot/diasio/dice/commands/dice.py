import nextcord
from nextcord.ext import commands
import random
from src.templates import embeds


class Dice(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(
        name="diasio-dice",
        description="Generate a random number.",
        force_global=True
    )
    async def dice(self, ctx: nextcord.Interaction, first_number: int, second_number: int):
        if first_number >= second_number:
            return await ctx.send("First number must be higher than the second number.", ephemeral=True)

        ran_num = random.randint(first_number, second_number)

        embed_random_number = embeds.TemplateEmbed(
            bot=self.bot,
            ctx=ctx,
            description="Fun | Diasio",
            color=nextcord.Color.orange()
        )
        embed_random_number.add_field(name="Random Number", value=ran_num)
        await ctx.send(embed=embed_random_number, ephemeral=True)


def setup(bot):
    bot.add_cog(Dice(bot))
