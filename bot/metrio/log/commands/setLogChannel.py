import nextcord
from nextcord.ext import commands
from src.dictionaries import logs


class SetLogChannel(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(
        name="metrio-set-log-channel",
        description="Set a channel for logs.",
        force_global=True,
        default_member_permissions=8
    )
    async def set_log_channel(self, ctx: nextcord.Interaction, channel: nextcord.TextChannel):
        await logs.set_log_channel(server_id=ctx.guild.id, channel_id=channel.id)
        await ctx.send(f"Log channel set to: {channel}", ephemeral=True)


def setup(bot):
    bot.add_cog(SetLogChannel(bot))
