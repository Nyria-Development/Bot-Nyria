import nextcord
from nextcord.ext import commands
from templates import embeds


class Kick(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(
        name="metrio-kick",
        description="Kick any member from the discord server.",
        force_global=True,
        default_member_permissions=8
    )
    async def kick(self, ctx: nextcord.Interaction, user: nextcord.Member, reason: str):
        await ctx.guild.kick(user=user, reason=reason)

        embed_kick = embeds.TemplateEmbed(
            bot=self.bot,
            ctx=ctx,
            description="Moderation | Metrio",
            color=nextcord.Color.red()
        )
        embed_kick.add_field(name=f"Kicked from {ctx.guild} | Reason", value=reason)
        await user.send(embed=embed_kick)


def setup(bot):
    bot.add_cog(Kick(bot))
