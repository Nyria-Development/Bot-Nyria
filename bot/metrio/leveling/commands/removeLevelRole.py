import nextcord
import json
from nextcord.ext import commands
from src.loader.jsonLoader import Leveling, LevelRoles

class Dropdown(nextcord.ui.Select):
    def __init__(self, ctx: nextcord.Interaction):
        options = []
        for role in LevelRoles().get_Roles()[str(ctx.guild.id)]:
            options.append(nextcord.SelectOption(label=role['name']))
        super().__init__(placeholder="Level Roles", min_values=1, max_values=1, options=options)

    async def callback(self, ctx: nextcord.Interaction):
        for role in LevelRoles().get_Roles()[str(ctx.guild.id)]:
            if self.values[0] == role['name']:
                level_role = ctx.guild.get_role(role['roleID'])
                await level_role.delete()
                delete_role_embed = nextcord.Embed(title=f"A Role was deleted",
                                                   description=f"The Role {role['name']} was deleted")
                delete_role_embed.add_field(name="Role: ", value=role['name'])
                delete_role_embed.add_field(name="Level: ", value=role['level'])
                self.write_into_file(ctx, role['name'])
                await ctx.send(embed=delete_role_embed)
                break

    def write_into_file(self, ctx, role_name):
        level_role_list = LevelRoles().get_Roles()
        level_role_list[str(ctx.guild.id)] = [role for role in level_role_list[str(ctx.guild.id)] if role['name'] != role_name]
        with open('resources/information/levelRoles.json', 'w') as file:
            json.dump(level_role_list, file, indent=4)

class DropdownView(nextcord.ui.View):
    def __init__(self, ctx):
        super().__init__()
        self.add_item(Dropdown(ctx))


class removeLevelRole(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(
        name="metrio-remove-level-role",
        description="Remove a Role for a Level",
        force_global=True,
        default_member_permissions=8
    )
    async def remove_role(self, ctx: nextcord.Interaction):
        delete_role_embed = nextcord.Embed(title=f"Remove a Role",
                                           description=f"Please select a role, that should be deleted")
        view=DropdownView(ctx)
        await ctx.send(embed=delete_role_embed, view=view, ephemeral=True)



def setup(bot):
    bot.add_cog(removeLevelRole(bot))
