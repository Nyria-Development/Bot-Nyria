import nextcord
from nextcord.ext import commands


class Ai(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(
        name="noirio-ai",
        description="Configure and control the bot over chatting.",
        force_global=True
    )
    async def ai(self, ctx: nextcord.Interaction, control: str):
        pass


def setup(bot):
    bot.add_cog(Ai(bot))
