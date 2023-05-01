import nextcord
from nextcord.ext import commands
from src.logger.logger import Logging
from src.templates.embeds.ctxEmbed import CtxEmbed


class Kick(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(
        name="metrio-kick",
        description="Kick user from your guild",
        force_global=True,
        default_member_permissions=8
    )
    async def kick(
            self,
            ctx: nextcord.Interaction,
            user: nextcord.Member = nextcord.SlashOption(
                description="The user you want to kick.",
                required=True
            ),
            reason: str = nextcord.SlashOption(
                description="Why you want to kick the user?",
                required=False
            )
    ) -> None:

        """
        Attributes
        ----------
        :param ctx:
        :param user:
        :param reason:
        :return: None
        ----------
        """

        Logging().info(f"Command :: metrio-kick :: {ctx.guild.name} :: {ctx.user}")

        await ctx.guild.kick(
            user=user,
            reason=reason
        )

        embed_kick = CtxEmbed(
            bot=self.bot,
            ctx=ctx,
            color=nextcord.Color.red(),
            description="Metrio | Moderation"
        )
        embed_kick.add_field(
            name=f"Kicked from {ctx.guild}",
            value=reason
        )
        await ctx.send(embed=embed_kick, ephemeral=True)


def setup(bot):
    bot.add_cog(Kick(bot))
