import nextcord
import math
from nextcord.ext import commands
from src.loader import jsonLoader


class getLevel(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(
        name="metrio-discord-level",
        description="Get the Level of you or someone from DC",
        force_global=True,
        default_member_permissions=8
    )
    async def getLevel(self, ctx: nextcord.Interaction, discord_user: nextcord.Member = nextcord.SlashOption(required=False)):
        if not discord_user:
            discord_user = ctx.user
        user_list = sorted(jsonLoader.Leveling().get_levels(), key=lambda d: d['xp'], reverse=True)
        if any(user['discordUserID'] == discord_user.id for user in user_list):
            for i, user in enumerate(user_list):
                if user['discordUserID'] == discord_user.id:
                    level_embed = nextcord.Embed(title="Level",
                                       description=f"Infos for {discord_user.mention}",
                                       color=0x081e8c)
                    level_embed.set_thumbnail(discord_user.display_avatar)
                    level_embed.add_field(name="Rank: ", value=f"#{i+1}")
                    level_embed.add_field(name="Level:", value=user['level'])
                    level_embed.add_field(name="XP:", value=user['xp'])
                    level_embed.add_field(name="XP to next Level:", value=self.getXPtoLevel(user))
                    await ctx.send(embed=level_embed, ephemeral=False)
                    break
        else:
            await ctx.send(f"The User {discord_user.mention} does not have any XP yet.", ephemeral=True)

    def getXPtoLevel(self, user):
        next_level = pow(2, user['level'])
        xp_to_level = (next_level - user['xp'])
        xp_to_level_procent = (1-(xp_to_level / next_level))*100
        xp_to_level_str = ":" * (math.floor(xp_to_level_procent/5)) + "." * (20 - (math.floor(xp_to_level_procent/5))) + f" - {xp_to_level} ({round(xp_to_level_procent)}%)"
        return xp_to_level_str





def setup(bot):
    bot.add_cog(getLevel(bot))
