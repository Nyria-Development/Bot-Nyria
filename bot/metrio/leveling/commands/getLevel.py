import nextcord
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
        user_list = jsonLoader.Leveling().get_levels()
        print(user_list, discord_user)
        if any(user['discordUserID'] == discord_user.id for user in user_list):
            for user in user_list:
                if user['discordUserID'] == discord_user.id:
                    level_embed = nextcord.Embed(title="Level",
                                       description=f"Infos for {discord_user.mention}",
                                       color=0x081e8c)
                    level_embed.add_field(name="Level:", value=user['level'])
                    level_embed.add_field(name="XP:", value=user['xp'])
                    level_embed.add_field(name="XP to next Level:", value=(pow(2, user['level']+1)-user['xp']))
                    await ctx.send(embed=level_embed, ephemeral=False)
                    break
        else:
            await ctx.send(f"The User {discord_user.mention} does not have any XP yet.", ephemeral=True)





def setup(bot):
    bot.add_cog(getLevel(bot))
