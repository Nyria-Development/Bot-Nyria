from typing import Union

import nextcord
from nextcord import PartialInteractionMessage, WebhookMessage
from nextcord.ext import commands
from src.logger.logger import Logging
from src.templates.embeds.ctxEmbed import CtxEmbed
from src.settings.logs import settingLogs
from src.database.tables.setup import LogsTable
from src.database.core.engine import SQLEngine
from src.database.core.session import SQLSession
from sqlalchemy import select, update


class LogSetup(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    async def create_embed(
            self,
            ctx: nextcord.Interaction,
            log_channel: nextcord.TextChannel,
            log_config_list: list
    ) -> nextcord.Embed:
        """
        Attributes
        ----------
        :param log_config_list:
        :param ctx:
        :param log_channel:
        :return: nextcord.Embed
        ----------
        """

        embed = CtxEmbed(
            bot=self.bot,
            ctx=ctx,
            color=nextcord.Color.blue(),
            description="Metrio | Moderation"
        )

        embed.add_field(
            name="Log channel",
            value=log_channel.mention,
            inline=False
        )
        for i, config in enumerate(log_config_list):
            embed.add_field(
                name=settingLogs.config_log_list[i],
                value=config
            )

        return embed

    @nextcord.slash_command(
        name="pyrio-setup-logs",
        description="Configue the log system",
        force_global=True,
        default_member_permissions=8
    )
    async def setup_logs(
            self,
            ctx: nextcord.Interaction,
            log_channel: nextcord.TextChannel = nextcord.SlashOption(
                description="The channel you send the log messages.",
                required=True
            ),
            on_message: str = nextcord.SlashOption(
                description="Logs when user send a message",
                choices=["on", "off"],
                required=False
            ),
            on_message_edit: str = nextcord.SlashOption(
                description="Logs when user edits a message",
                choices=["on", "off"],
                required=False
            ),
            on_message_delete: str = nextcord.SlashOption(
                description="Logs when user deletes a message",
                choices=["on", "off"],
                required=False
            ),
            on_reaction_add: str = nextcord.SlashOption(
                description="Logs when user adds a reaction",
                choices=["on", "off"],
                required=False
            ),
            on_reaction_remove: str = nextcord.SlashOption(
                description="Logs when user removes a reaction",
                choices=["on", "off"],
                required=False
            ),
            on_member_ban: str = nextcord.SlashOption(
                description="Logs when user banned from the server",
                choices=["on", "off"],
                required=False
            ),
            on_member_unban: str = nextcord.SlashOption(
                description="Logs when user was unbanned from the server",
                choices=["on", "off"],
                required=False
            )
    ) -> Union[PartialInteractionMessage, WebhookMessage]:
        """
        Attributes
        ----------
        :param on_reaction_remove:
        :param ctx:
        :param log_channel:
        :param on_message:
        :param on_message_edit:
        :param on_message_delete:
        :param on_reaction_add:
        :param on_member_ban:
        :param on_member_unban:
        :return: None
        ----------
        """

        Logging().info(f"Command :: pyrio-setup-logs :: {ctx.guild.name} :: {ctx.user}")

        db_conn = SQLEngine.engine.connect()

        query = select(LogsTable).where(LogsTable.server_id == ctx.guild.id)
        log_configuration = db_conn.execute(query).all()

        if not log_configuration:
            log_config_list = [on_message if on_message else "off",
                               on_message_edit if on_message_edit else "off",
                               on_message_delete if on_message_delete else "off",
                               on_reaction_add if on_reaction_add else "off",
                               on_reaction_remove if on_reaction_remove else "off",
                               on_member_ban if on_member_ban else "off",
                               on_member_unban if on_member_unban else "off"]  # gleicher Reihenfolge wie bei settingsLog.py

            db_session = SQLSession.create_session()

            await settingLogs.create_log(
                server_id=ctx.guild.id,
                log_channel_id=log_channel.id,
                log_config_list=log_config_list
            )

            logs = LogsTable(
                server_id=ctx.guild.id,
                log_channel_id=log_channel.id,
                log_config_int=settingLogs.get_logs(ctx.guild.id)['log_config_int']
            )
            db_session.add(logs)
            db_session.commit()
            db_session.close()
            db_conn.close()

            embed_setup_logs = await self.create_embed(
                ctx=ctx,
                log_channel=log_channel,
                log_config_list=log_config_list
            )

            return await ctx.send(embed=embed_setup_logs, ephemeral=True)

        logs = settingLogs.get_logs_on_off(guild_id=ctx.guild.id)
        log_config_list = [on_message if on_message else logs['on_message'],
                           on_message_edit if on_message_edit else logs['on_message_edit'],
                           on_message_delete if on_message_delete else logs['on_message_delete'],
                           on_reaction_add if on_reaction_add else logs['on_reaction_add'],
                           on_reaction_remove if on_reaction_remove else logs['on_reaction_remove'],
                           on_member_ban if on_member_ban else logs['on_member_ban'],
                           on_member_unban if on_member_unban else logs['on_member_unban']]  # gleicher Reihenfolge wie bei settingsLog.py

        await settingLogs.create_log(
            server_id=ctx.guild.id,
            log_channel_id=log_channel.id,
            log_config_list=log_config_list
        )

        query = update(LogsTable).values(
            log_channel_id=log_channel.id,
            log_config_int=settingLogs.get_logs(ctx.guild.id)['log_config_int']
        ).where(LogsTable.server_id == ctx.guild.id)
        db_conn.execute(query)
        db_conn.commit()
        db_conn.close()

        embed_setup_logs = await self.create_embed(
            ctx=ctx,
            log_channel=log_channel,
            log_config_list=log_config_list
        )

        await ctx.send(embed=embed_setup_logs, ephemeral=True)


def setup(bot):
    bot.add_cog(LogSetup(bot))
