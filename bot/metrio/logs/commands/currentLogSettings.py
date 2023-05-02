import nextcord
from nextcord import PartialInteractionMessage, WebhookMessage
from nextcord.ext import commands
from src.logger.logger import Logging
from src.settings.logs import settingLogs
from src.templates.embeds.ctxEmbed import CtxEmbed


class CurrentLogSetting(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(
        name="metrio-log-current-settings",
        description="Show the current log settings",
        force_global=True,
        default_member_permissions=8
    )
    async def log_current_settings(
            self,
            ctx: nextcord.Interaction
    ) -> PartialInteractionMessage | WebhookMessage:

        """
        Attributes
        ----------
        :param ctx:
        :return: None
        ----------
        """

        Logging().info(f"Command :: metrio-log-current-settings :: {ctx.guild.name} :: {ctx.user}")

        logs = await settingLogs.get_logs(
            guild_id=ctx.guild.id
        )
        if logs is False:
            return await ctx.send("The log system is not available on this server.")

        embed_current_setting_logs = CtxEmbed(
            bot=self.bot,
            ctx=ctx,
            color=nextcord.Color.red(),
            description="Metrio | Moderation"
        )

        log_channel = self.bot.get_channel(logs["log_channel_id"])
        embed_current_setting_logs.add_field(
            name="Log channel",
            value=log_channel.name,
            inline=False
        )
        embed_current_setting_logs.add_field(
            name="Message log",
            value=logs["on_message"]
        )
        embed_current_setting_logs.add_field(
            name="Message edit log",
            value=logs["on_message_edit"]
        )
        embed_current_setting_logs.add_field(
            name="Message delete log",
            value=logs["on_message_delete"],
            inline=False
        )
        embed_current_setting_logs.add_field(
            name="Reaction log",
            value=logs["on_reaction_add"]
        )
        embed_current_setting_logs.add_field(
            name="Member ban log",
            value=logs["on_member_ban"]
        )
        embed_current_setting_logs.add_field(
            name="Member unban log",
            value=logs["on_member_unban"]
        )

        await ctx.send(embed=embed_current_setting_logs, ephemeral=True)


def setup(bot):
    bot.add_cog(CurrentLogSetting(bot))
