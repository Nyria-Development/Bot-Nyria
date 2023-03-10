import nextcord
from nextcord.ext import commands
from src.dictionaries import level


class getLeveling(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(
        name="metrio-discord-get-leveling",
        description="Get Your leveling Settings on Discord",
        force_global=True,
        default_member_permissions=8
    )
    async def setLeveling(self, ctx: nextcord.Interaction):
        leveling_status = level.get_leveling_server(ctx.guild_id)
        if leveling_status:
            await ctx.send(f"Leveling is active with a speed of: {leveling_status}", ephemeral=True)
        else:
            await ctx.send(f"Leveling is deactivated", ephemeral=True)





def setup(bot):
    bot.add_cog(getLeveling(bot))
