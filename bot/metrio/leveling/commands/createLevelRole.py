import nextcord
import json
from nextcord.ext import commands
from src.loader.jsonLoader import Leveling, LevelRoles


class createLevelRole(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.colour_dic = {"white": 0xFFFFFF, "Greyple": 0x99AAb5, "Black": 0x23272A, "DarkButNotBlack": 0x2C2F33, "NotQuiteBlack": 0x23272A, "Blurple": 0x5865F2, "Green": 0x57F287, "Yellow": 0xFEE75C, "Fuchsia": 0xEB459E, "Red": 0xED4245}

    @nextcord.slash_command(
        name="metrio-create-level-role",
        description="Create your own Role for a Level",
        force_global=True,
        default_member_permissions=8
    )
    async def create_role(self, ctx: nextcord.Interaction, role_name: str, level: int, colour: str = nextcord.SlashOption(choices=list({"white": 0xFFFFFF, "Greyple": 0x99AAb5, "Black": 0x23272A, "DarkButNotBlack": 0x2C2F33, "NotQuiteBlack": 0x23272A, "Blurple": 0x5865F2, "Green": 0x57F287, "Yellow": 0xFEE75C, "Fuchsia": 0xEB459E, "Red": 0xED4245}.keys()))):
        new_level_role = await ctx.guild.create_role(name=role_name, color=self.colour_dic[colour])
        new_role_embed = nextcord.Embed(title=f"The Level Role, {new_level_role}, was created",
                                        description=f"A New Role from Level {level} was created")
        new_role_embed.add_field(name="Role: ", value=new_level_role.mention)
        new_role_embed.add_field(name="Level: ", value=level)
        self.write_into_file(ctx.guild, new_level_role, level)
        await self.sync_member_level(ctx.guild, new_level_role, level)
        await ctx.send(embed=new_role_embed)

    async def sync_member_level(self, guild, level_role, level):
        user_list = sorted(Leveling().get_levels(), key=lambda d: d['xp'], reverse=True)
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
    bot.add_cog(createLevelRole(bot))
