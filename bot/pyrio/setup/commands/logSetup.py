# All Rights Reserved
# Copyright (c) 2023 Nyria
#
# This code, including all accompanying software, documentation, and related materials, is the exclusive property
# of Nyria. All rights are reserved.
#
# Any use, reproduction, distribution, or modification of the code without the express written
# permission of Nyria is strictly prohibited.
#
# No warranty is provided for the code, and Nyria shall not be liable for any claims, damages,
# or other liability arising from the use or inability to use the code.

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
            on_role_add: str = nextcord.SlashOption(
                description="Logs when user removes a reaction",
                choices=["on", "off"],
                required=False
            ),
            on_role_remove: str = nextcord.SlashOption(
                description="Logs when user removes a reaction",
                choices=["on", "off"],
                required=False
            ),
            on_role_update: str = nextcord.SlashOption(
                description="Logs when user removes a reaction",
                choices=["on", "off"],
                required=False
            ),
            on_role_create: str = nextcord.SlashOption(
                description="Logs when user removes a reaction",
                choices=["on", "off"],
                required=False
            ),
            on_role_delete: str = nextcord.SlashOption(
                description="Logs when user removes a reaction",
                choices=["on", "off"],
                required=False
            ),
            on_channel_create: str = nextcord.SlashOption(
                description="Logs when user removes a reaction",
                choices=["on", "off"],
                required=False
            ),
            on_channel_delete: str = nextcord.SlashOption(
                description="Logs when user removes a reaction",
                choices=["on", "off"],
                required=False
            ),
            on_channel_update: str = nextcord.SlashOption(
                description="Logs when user removes a reaction",
                choices=["on", "off"],
                required=False
            ),
            on_member_update_nick: str = nextcord.SlashOption(
                description="Logs when user removes a reaction",
                choices=["on", "off"],
                required=False
            ),
            on_member_update_avatar: str = nextcord.SlashOption(
                description="Logs when user removes a reaction",
                choices=["on", "off"],
                required=False
            ),
            on_member_join: str = nextcord.SlashOption(
                description="Logs when user removes a reaction",
                choices=["on", "off"],
                required=False
            ),
            on_member_leave: str = nextcord.SlashOption(
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
    ) -> PartialInteractionMessage | WebhookMessage:
        """
        Attributes
        ----------
        :param on_channel_update:
        :param on_channel_delete:
        :param on_channel_create:
        :param ctx:
        :param on_role_add:
        :param on_role_remove:
        :param on_role_update:
        :param on_role_create:
        :param on_role_delete:
        :param on_member_update_avatar:
        :param on_member_update_nick:
        :param on_member_join:
        :param on_member_leave:
        :param on_reaction_remove:
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
                               on_role_add if on_role_add else "off",
                               on_role_remove if on_role_remove else "off",
                               on_role_update if on_role_update else "off",
                               on_role_create if on_role_create else "off",
                               on_role_delete if on_role_delete else "off",
                               on_channel_create if on_channel_create else "off",
                               on_channel_delete if on_channel_delete else "off",
                               on_channel_update if on_channel_update else "off",
                               on_member_update_nick if on_member_update_nick else "off",
                               on_member_update_avatar if on_member_update_avatar else "off",
                               on_member_join if on_member_join else "off",
                               on_member_leave if on_member_leave else "off",
                               on_member_ban if on_member_ban else "off",
                               on_member_unban if on_member_unban else "off"]

            db_session = SQLSession.create_session()

            await settingLogs.create_log(
                bot=self.bot,
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
        # same order as in settingsLog.py
        log_config_list = [on_message if on_message else logs['on_message'],
                           on_message_edit if on_message_edit else logs['on_message_edit'],
                           on_message_delete if on_message_delete else logs['on_message_delete'],
                           on_reaction_add if on_reaction_add else logs['on_reaction_add'],
                           on_reaction_remove if on_reaction_remove else logs['on_reaction_remove'],
                           on_role_add if on_role_add else logs['on_role_add'],
                           on_role_remove if on_role_remove else logs['on_role_remove'],
                           on_role_update if on_role_update else logs['on_role_update'],
                           on_role_create if on_role_create else logs['on_role_create'],
                           on_role_delete if on_role_delete else logs['on_role_delete'],
                           on_channel_create if on_channel_create else logs['on_channel_create'],
                           on_channel_delete if on_channel_delete else logs['on_channel_delete'],
                           on_channel_update if on_channel_update else logs['on_channel_update'],
                           on_member_update_nick if on_member_update_nick else logs['on_member_update_nick'],
                           on_member_update_avatar if on_member_update_avatar else logs['on_member_update_avatar'],
                           on_member_join if on_member_join else logs['on_member_join'],
                           on_member_leave if on_member_leave else logs['on_member_leave'],
                           on_member_ban if on_member_ban else logs['on_member_ban'],
                           on_member_unban if on_member_unban else logs['on_member_unban']]

        await settingLogs.create_log(
            bot=self.bot,
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
