import nextcord
import math

from nextcord import PartialInteractionMessage, WebhookMessage
from nextcord.ext import commands
from src.loader.jsonLoader import Leveling


class GetLevel(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(
        name="metrio-discord-level",
        description="Get the Level of you or someone from DC",
        force_global=True,
        default_member_permissions=8
    )
    async def get_level(
            self,
            ctx: nextcord.Interaction,
            discord_user: nextcord.Member = nextcord.SlashOption(required=False)
    ) -> PartialInteractionMessage | WebhookMessage:

        """
        Attributes
        ----------
        :param ctx: Gives the discord interaction
        :param discord_user: Gives the user to get the level system. If "None" uses yourself
        :return: None
        ----------
        """

        if not discord_user:
            discord_user = ctx.user

        user_list = sorted(Leveling().get_levels(), key=lambda d: d['xp'], reverse=True)

        if not any(user['discordUserID'] == discord_user.id for user in user_list):
            return await ctx.send(f"The User {discord_user.mention} does not have any XP yet.", ephemeral=True)

        for i, user in enumerate(user_list):
            if user['discordUserID'] == discord_user.id:

                level_embed = nextcord.Embed(
                    title="Level",
                    description=f"Infos for {discord_user.mention}",
                    color=0x081e8c
                )

                level_embed.set_thumbnail(discord_user.display_avatar)
                level_embed.add_field(name="Rank: ", value=f"#{i + 1}")
                level_embed.add_field(name="Level:", value=user['level'])
                level_embed.add_field(name="XP:", value=user['xp'])
                level_embed.add_field(name="XP to next Level:", value=self.getXPtoLevel(user))

                await ctx.send(embed=level_embed, ephemeral=False)
                break

    def getXPtoLevel(self, user):
        next_level = pow(2, user['level'])
        xp_to_level = (next_level - user['xp'])
        xp_to_level_procent = (1 - (xp_to_level / next_level)) * 100
        xp_to_level_str = ":" * (math.floor(xp_to_level_procent / 5)) + "." * (
                    20 - (math.floor(xp_to_level_procent / 5))) + f" - {xp_to_level} ({round(xp_to_level_procent)}%)"
        return xp_to_level_str


def setup(bot):
    bot.add_cog(GetLevel(bot))
