import nextcord
from nextcord.ext import commands
from src.templates import embeds


class Unban(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(
        name="metrio-unban",
        description="Unban a member",
        force_global=True,
        default_member_permissions=8
    )
    async def unban(self, ctx: nextcord.Interaction, user: nextcord.Member):
        await ctx.guild.unban(user=user)

        embed_unban = embeds.TemplateEmbed(
            bot=self.bot,
            ctx=ctx,
            description="Moderation | Metrio",
            color=nextcord.Color.red()
        )
        embed_unban.add_field(
            name="User unbanned",
            value=user
        )
        await user.send(embed=embed_unban)


def setup(bot):
    bot.add_cog(Unban(bot))
