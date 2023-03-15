import nextcord
from nextcord.ext import commands
from src.loader.jsonLoader import LevelRoles
import json


class Roles(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_role_update(self, before: nextcord.Role, after: nextcord.Role):
        if any(role['roleID'] == after.id for role in LevelRoles().get_Roles()[str(after.guild.id)]):
            level_role_list = LevelRoles().get_Roles()
            for i, role in enumerate(level_role_list[str(after.guild.id)]):
                if role['roleID'] == after.id:
                    level_role_list[str(after.guild.id)][i]['name'] = after.name
                    break
            with open('resources/information/levelRoles.json', 'w') as file:
                json.dump(level_role_list, file, indent=4)





def setup(bot):
    bot.add_cog(Roles(bot))
