import nextcord
from nextcord.ext import commands


class Dropdown(nextcord.ui.Select):
    def __init__(self, command_list, list_of_modules, depth):
        self.command_list = command_list
        self.list_of_modules = list_of_modules
        self.depth = depth
        options = [nextcord.SelectOption(label="Home")]
        if self.depth == "modules":
            for option in self.list_of_modules:
                options.append(nextcord.SelectOption(label=option))
        elif any(module == self.depth for module in self.list_of_modules):
            for command in self.command_list:
                if command['module'] == depth:
                    options.append(nextcord.SelectOption(label=command['command_name']))
        else:
            options.append(nextcord.SelectOption(label=str([command['module'] for command in self.command_list if command['command_name'] == self.depth][0])))
        super().__init__(placeholder=self.depth, min_values=1, max_values=1, options=options)

    async def callback(self, interaction: nextcord.Interaction):
        self.depth = str(self.values[0])
        if self.depth == "Home":
            await interaction.edit(embed=self.get_embed(), view=DropdownView(self.command_list, self.list_of_modules, "modules"))
        else:
            await interaction.edit(embed=self.get_embed(), view=DropdownView(self.command_list, self.list_of_modules, self.depth))


    def get_embed(self):
        if any(module == self.depth for module in self.list_of_modules):
            help_embed = nextcord.Embed(title=f"Command List: {self.depth}",
                                        description=f"List of all commands in {self.depth}. Please select a command for more information:",
                                        color=0x081e8c)
        elif self.depth == "Home":
            help_embed = nextcord.Embed(title=f"Command List",
                                        description=f"Please select a Module for more information:",
                                        color=0x081e8c)
        else:
            help_embed = nextcord.Embed(title=f"Command Info: {self.depth}",
                                        description=f"Information to {self.depth}:",
                                        color=0x081e8c)
            help_embed.add_field(name="Command Name:", value=[command['command_name'] for command in self.command_list if command['command_name'] == self.depth][0])
            help_embed.add_field(name="Command Description:", value=[command['description'] for command in self.command_list if command['command_name'] == self.depth][0])
        help_embed.set_footer(text=self.depth)
        return help_embed

class DropdownView(nextcord.ui.View):
    def __init__(self, command_list, list_of_modules, depth):
        super().__init__()
        self.add_item(Dropdown(command_list, list_of_modules, depth))


class CommandList(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(name="metrio-list-commands", description="List of all commands. Seconde Function",
                            force_global=True)
    async def command_list(self, ctx: nextcord.Interaction):
        command_list = self.load_command_list()
        list_of_modules = list({command['module']: command['module'] for command in command_list}.values())
        help_embed = nextcord.Embed(title="Command List",
                                    description=f"list of all commands. Pls Select:",
                                    color=0x081e8c)
        help_embed.set_footer(text="Home")
        view = DropdownView(command_list, list_of_modules, "modules")
        await ctx.response.send_message(embed=help_embed, view=view, ephemeral=True)

    def load_command_list(self):
        command_list_loader = self.bot.get_all_application_commands()
        command_list = []
        for command in command_list_loader:
            new_command = {"module": command.name.split("-")[0], "command_name": command.name,
                           "description": command.description, "options": command.options}
            command_list.append(new_command)
        return sorted(command_list, key=lambda d: d['module'])


def setup(bot):
    bot.add_cog(CommandList(bot))
