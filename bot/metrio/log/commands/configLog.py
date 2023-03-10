import nextcord
from nextcord.ext import commands
from src.dictionaries import logs


class ConfigLog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(
        name="metrio-confi-log-settings",
        description="Configurate the log settings for your discord.",
        force_global=True,
        default_member_permissions=8
    )
    async def config_log_settings(self, ctx: nextcord.Interaction,
                                  log_channel: nextcord.TextChannel,
                                  log: str = nextcord.SlashOption(choices=["activate", "deactivate"]),
                                  message_log: int = nextcord.SlashOption(choices=[1, 0], default=1, required=False),
                                  reaction_log: int = nextcord.SlashOption(choices=[1, 0], default=1, required=False),
                                  on_member_log: int = nextcord.SlashOption(choices=[1, 0], default=1, required=False)):
        await logs.config_log_settings(server_id=ctx.guild.id, log_channel_id=log_channel.id, log=log, message_log=message_log, reaction_log=reaction_log, on_member_log=on_member_log)
        log_config_embed = nextcord.Embed(title="Log-Config", description="Your Log settings where updated", color=0x081e8c)
        log_config_embed.add_field(name="log is:", value=log)
        if log == "activate":
            log_config_embed.add_field(name="Log Channel: ", value=log_channel.mention)
            log_config_embed.add_field(name="Message Log: ", value=message_log)
            log_config_embed.add_field(name="Reaction Log: ", value=reaction_log)
            log_config_embed.add_field(name="On Member Events Log: ", value=on_member_log)
        await ctx.send(embed=log_config_embed, ephemeral=True)


def setup(bot):
    bot.add_cog(ConfigLog(bot))
