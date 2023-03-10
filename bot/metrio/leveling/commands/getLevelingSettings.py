import nextcord
from nextcord import PartialInteractionMessage, WebhookMessage
from nextcord.ext import commands
from src.dictionaries import level


class GetLeveling(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(
        name="metrio-discord-get-leveling",
        description="Get Your leveling Settings on Discord",
        force_global=True,
        default_member_permissions=8
    )
    async def get_leveling(
            self,
            ctx: nextcord.Interaction
    ) -> PartialInteractionMessage | WebhookMessage:

        leveling_status = level.get_leveling_server(ctx.guild_id)

        if not leveling_status:
            return await ctx.send(f"Leveling is deactivated", ephemeral=True)

        await ctx.send(f"Leveling is active with a speed of: {leveling_status}", ephemeral=True)


def setup(bot):
    bot.add_cog(GetLeveling(bot))
