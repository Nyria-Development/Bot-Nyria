import nextcord
import json
from nextcord.ext import commands
from src.loader.jsonLoader import Leveling, LevelRoles


class setLevelRole(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.colour_dic = {"white": 0xFFFFFF, "Greyple": 0x99AAb5, "Black": 0x23272A, "DarkButNotBlack": 0x2C2F33, "NotQuiteBlack": 0x23272A, "Blurple": 0x5865F2, "Green": 0x57F287, "Yellow": 0xFEE75C, "Fuchsia": 0xEB459E, "Red": 0xED4245}

    @nextcord.slash_command(
        name="metrio-set-level-role",
        description="Set a Role for a Level",
        force_global=True,
        default_member_permissions=8
    )
    async def setLevelRole(self, ctx: nextcord.Interaction, level_role: nextcord.Role, level: int):
        if not any(role['name'] == str(level_role.name) for role in LevelRoles().get_Roles()[str(ctx.guild_id)]):
            new_role_embed = nextcord.Embed(title=f"Set Level Role",
                                            description=f"{level_role.mention} was set to Level {level}")
            new_role_embed.add_field(name="Role: ", value=level_role.mention)
            new_role_embed.add_field(name="Level: ", value=level)
            self.write_into_file(ctx.guild, level_role, level)
            await self.sync_member_level(ctx, ctx.guild, level_role, level)
            await ctx.send(embed=new_role_embed)
        else:
            new_role_embed = nextcord.Embed(title=f"A Level Role with the Name {level_role.name} already is set",
                                            description=f"Name already used")
            await ctx.send(embed=new_role_embed, ephemeral=True)

    async def sync_member_level(self, ctx, guild, level_role, level):
        user_list = sorted(Leveling().get_levels()[str(ctx.guild_id)], key=lambda d: d['xp'], reverse=True)
        for user in user_list:
            if user['level'] >= level:
                discord_user = guild.get_member(user['discordUserID'])
                await discord_user.add_roles(level_role)

    def write_into_file(self, guild, level_role: nextcord.Role, level):
        level_roles = LevelRoles().get_Roles()
        if any(str(guild_id) == str(guild.id) for guild_id in level_roles):
            level_roles[f'{guild.id}'].append({"roleID": level_role.id, "name": level_role.name, "level": level})
        else:
            new_guild = {f'{guild.id}': [{"roleID": level_role.id, "name": level_role.name, "level": level}]}
            level_roles.update(new_guild)
        with open('resources/information/levelRoles.json', 'w') as file:
            json.dump(level_roles, file, indent=4)



def setup(bot):
    bot.add_cog(setLevelRole(bot))
