import nextcord
from nextcord.ext import commands
from src.dictionaries import logs


class getConfigLog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(
        name="metrio-get-log-settings",
        description="Get the log settings for your discord.",
        force_global=True,
        default_member_permissions=8
    )
    async def get_log_settings(self, ctx: nextcord.Interaction):
        if logs.get_log_channel(ctx.guild_id):
            log_config_embed = nextcord.Embed(title="Log-Config", description="Your Log settings", color=0x081e8c)
            log_config_embed.add_field(name="log is:", value=("on" if logs.get_log_on_state(ctx.guild_id, 1) == 1 else "off"))
            if logs.get_log_on_state(ctx.guild_id, 1) == 1:
                log_channel = await self.bot.fetch_channel(logs.get_log_on_state(ctx.guild_id, 0))
                log_config_embed.add_field(name="Log Channel: ", value=log_channel.mention)
                log_config_embed.add_field(name="Message Log: ", value=logs.get_log_on_state(ctx.guild_id, 2))
                log_config_embed.add_field(name="Reaction Log: ", value=logs.get_log_on_state(ctx.guild_id, 3))
                log_config_embed.add_field(name="On Member Events Log: ", value=logs.get_log_on_state(ctx.guild_id, 4))
        else:
            log_config_embed = nextcord.Embed(title="Log-Config", description="Your Log isnt set up.",
                                              color=0x081e8c)
        await ctx.send(embed=log_config_embed, ephemeral=True)


def setup(bot):
    bot.add_cog(getConfigLog(bot))
