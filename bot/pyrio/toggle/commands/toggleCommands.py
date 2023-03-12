from nextcord.ext import commands


class ToggleCommands(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot


def setup(bot):
    bot.add_cog(ToggleCommands(bot))
