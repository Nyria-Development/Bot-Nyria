import nextcord
from nextcord.ext import commands
from templates import embeds


class Bugs(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(
        name="pyrio-bug",
        description="You found a bug. Here you can report it.",
        force_global=True
    )
    async def bugs(self, ctx: nextcord.Interaction, bug: str):
        embed_bugs = embeds.TemplateEmbed(
            bot=self.bot,
            ctx=ctx,
            description="Core | Pyrio",
            color=nextcord.Color.brand_green()
        )
        embed_bugs.set_thumbnail(url=ctx.user.avatar)
        embed_bugs.add_field(name="Bug Description", value=bug)

        if len(bug) > 1024:
            return await ctx.send("This report is to long.", ephemeral=True)

        user = await self.bot.fetch_user(817657386751754251)
        await user.send(embed=embed_bugs)
        await ctx.send("Thanks for reporting.", ephemeral=True)


def setup(bot):
    bot.add_cog(Bugs(bot))
