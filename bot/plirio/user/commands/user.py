import nextcord
from nextcord.ext import commands
from src.templates import embeds


class UserStats(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(
        name="plirio-user-stats",
        description="Show server stats from a user.",
        force_global=True,
        default_member_permissions=8
    )
    async def user_stats(self, ctx: nextcord.Interaction, user: nextcord.Member):
        embed_user = embeds.TemplateEmbed(
            bot=self.bot,
            ctx=ctx,
            description="Information | Plirio",
            color=nextcord.Color.orange()
        )
        embed_user.add_field(name="User", value=user.mention)
        embed_user.add_field(name="Name", value=user.name)
        embed_user.add_field(name="Status", value=user.status)
        embed_user.add_field(name="Roles", value=", ".join([role.mention for role in user.roles]))
        embed_user.set_thumbnail(user.display_avatar)

        await ctx.send(embed=embed_user, ephemeral=True)


def setup(bot):
    bot.add_cog(UserStats(bot))
