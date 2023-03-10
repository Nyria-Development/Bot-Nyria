import nextcord
from nextcord.ext import commands
from src.loader import jsonLoader


class helpButton(nextcord.ui.View):
    def __init__(self, buttons_required, depth):
        super().__init__()
        self.depth = depth
        self.buttons_required = buttons_required
        self.nameList = ["category", "function", "command", "parameter"]
        self.button_list = [self.bt1, self.bt2, self.bt3, self.bt4, self.bt5]
        self.getButtonLabel()

    @nextcord.ui.button(label="Home", emoji="🏠", style=nextcord.ButtonStyle.grey)
    async def homeBt(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        self.depth.clear()
        self.buttons_required = 3 # 3: Number of set groups (diasio, kanio, metrio, etc) in commands.json
        self.getButtonLabel()
        await interaction.message.edit(embed=self.setEmbed(), view=self)

    @nextcord.ui.button(label="diasio", style=nextcord.ButtonStyle.green)
    async def bt1(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        self.depth.append(0)
        self.buttons_required = self.getButtonRequiered()
        self.getButtonLabel()
        await interaction.message.edit(embed=self.setEmbed(), view=self)

    @nextcord.ui.button(label="kanio", style=nextcord.ButtonStyle.green)
    async def bt2(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        self.depth.append(1)
        self.buttons_required = self.getButtonRequiered()
        self.getButtonLabel()
        await interaction.message.edit(embed=self.setEmbed(), view=self)

    @nextcord.ui.button(label="matrio", style=nextcord.ButtonStyle.green)
    async def bt3(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        self.depth.append(2)
        self.buttons_required = self.getButtonRequiered()
        self.getButtonLabel()
        await interaction.message.edit(embed=self.setEmbed(), view=self)

    @nextcord.ui.button(label="plirio", style=nextcord.ButtonStyle.green)
    async def bt4(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        self.depth.append(3)
        self.buttons_required = self.getButtonRequiered()
        self.getButtonLabel()
        await interaction.message.edit(embed=self.setEmbed(), view=self)

    @nextcord.ui.button(label="pyrio", style=nextcord.ButtonStyle.green)
    async def bt5(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        self.depth.append(4)
        self.buttons_required = self.getButtonRequiered()
        self.getButtonLabel()
        await interaction.message.edit(embed=self.setEmbed(), view=self)

    def getButtonLabel(self):
        for i, button in enumerate(self.button_list):
            if i < self.buttons_required:
                button.label = self.getLabel(i)
                button.disabled = False
            else:
                button.disabled = True

    def getSubList(self, commandList):
        subList = commandList[self.depth[0]]
        for i, number in enumerate(self.depth):
            if i > 0:
                subList = subList[f"{self.nameList[i]}s"][number]
        return subList

    def getLabel(self, button_id: int):
        commandList = jsonLoader.Commands().get_commands()
        if not self.depth:
            return f"{str(commandList[button_id]['categoryName'])}"
        else:
            sub_list = self.getSubList(commandList)
            return sub_list[f"{self.nameList[len(self.depth)]}s"][button_id][
                f"{self.nameList[len(self.depth)]}Name"]

    def getButtonRequiered(self):
        commandList = jsonLoader.Commands().get_commands()
        sub_list = self.getSubList(commandList)
        if len(self.depth) < 3:
            return len(sub_list[f"{self.nameList[len(self.depth) - 0]}s"])
        else:
            return 0

    def setEmbed(self):
        if self.depth:
            commandList = jsonLoader.Commands().get_commands()
            sub_list = self.getSubList(commandList)
            command_name = sub_list[f"{self.nameList[len(self.depth) - 1]}Name"]
            command_discription = sub_list[f"{self.nameList[len(self.depth) - 1]}Discription"]
            help_embed = nextcord.Embed(title=f"Help for: {command_name}",
                                        description=f"{command_name}: {command_discription}",
                                        color=0x081e8c)
            help_embed.add_field(name="Name", value=command_name)
            help_embed.add_field(name="Discription", value=command_discription)
            if len(self.depth) < 3:
                help_embed.add_field(name=f"Find out more about {self.nameList[len(self.depth)]}s in {command_name}", value="with a CLick on the Buttons", inline=False)
            if self.nameList[len(self.depth) - 1] == "command":
                help_embed.add_field(name=f"Command:",
                                     value=sub_list[self.nameList[len(self.depth) - 1]], inline=False)
            help_embed.set_footer(text=self.nameList[len(self.depth) - 1])
        else:
            help_embed = nextcord.Embed(title="Command List",
                                        description=f"list of all commands. Pls Select:",
                                        color=0x081e8c)
            help_embed.set_footer(text="Home")
        return help_embed


class CommandList(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(name="metrio-list-commands", description="List of all commands", force_global=True)
    async def test(self, ctx: nextcord.Interaction):
        help_embed = nextcord.Embed(title="Command List",
                                    description=f"list of all commands. Pls Select:",
                                    color=0x081e8c)
        help_embed.set_footer(text="Home")
        await ctx.response.send_message(embed=help_embed, view=helpButton(3, []))# 3: Number of set groups (diasio, kanio, metrio, etc) in commands.json


def setup(bot):
    bot.add_cog(CommandList(bot))
