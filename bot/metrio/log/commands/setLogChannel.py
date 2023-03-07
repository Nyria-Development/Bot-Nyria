import nextcord
from nextcord.ext import commands
from database.query import Query


class SetLogChannel(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.database = Query(
            pool_name="set_log_channel",
            pool_size=2
        )

    @nextcord.slash_command(
        name="metrio-set-log-channel",
        description="Set a channel for logs.",
        force_global=True,
        default_member_permissions=8
    )
    async def set_log_channel(self, ctx: nextcord.Interaction, channel: nextcord.TextChannel):
        log_channel_id = self.database.execute(
            query="SELECT channelId FROM logs WHERE serverId=%s",
            data=[int(ctx.guild.id)]
        )

        if not log_channel_id:
            self.database.execute(
                query="INSERT INTO logs (serverId, channelId) VALUE (%s,%s)",
                data=[int(ctx.guild.id), int(channel.id)]
            )
            return await ctx.send(f"Set log channel: **{channel.name}**", ephemeral=True)

        self.database.execute(
            query=f"UPDATE logs SET channelId={int(channel.id)} WHERE serverId=%s",
            data=[int(ctx.guild.id)]
        )

        await ctx.send(f"Log channel set to: **{channel.name}**", ephemeral=True)


def setup(bot):
    bot.add_cog(SetLogChannel(bot))
