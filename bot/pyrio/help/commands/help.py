import nextcord
from nextcord.ext import commands
import random
from src.templates import embeds


class help_command(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(
        name="pyrio-help",
        description="Generate a random number.",
        force_global=True
    )
    async def help_command(self, ctx: nextcord.Interaction):
        help_embed = embeds.TemplateEmbed(
            bot=self.bot,
            ctx=ctx,
            description="HELP | Nyria",
            color=nextcord.Color.orange()
        )
        help_embed.add_field(name="List of all Commands", value="/pyrio-list-commands")
        help_embed.add_field(name="Information to how to use the Bot", value="nyria-website/help (when Website is online: Link)")
        await ctx.send(embed=help_embed, ephemeral=True)


def setup(bot):
    bot.add_cog(help_command(bot))
