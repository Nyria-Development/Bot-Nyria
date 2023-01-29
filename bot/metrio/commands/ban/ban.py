import nextcord
from nextcord.ext import commands
from src.templates import embeds


class Ban(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(
        name="metrio-ban",
        description="Ban a member",
        force_global=True,
        default_member_permissions=8
    )
    async def ban(self, ctx: nextcord.Interaction, user: nextcord.Member, reason: str):
        await ctx.guild.ban(user=user, reason=reason)

        embed_ban = embeds.TemplateEmbed(
            bot=self.bot,
            ctx=ctx,
            description="Moderation | Metrio",
            color=nextcord.Color.red()
        )
        embed_ban.add_field(name=f"Banned from {ctx.guild} | Reason", value=reason)
        await user.send(embed=embed_ban)


def setup(bot):
    bot.add_cog(Ban(bot))
