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
            log_channel: str,
            on_message: str,
            on_message_edit: str,
            on_message_delete: str,
            on_reaction_add: str,
            on_member_ban: str,
            on_member_unban: str
    ) -> nextcord.Embed:

        """
        Attributes
        ----------
        :param ctx:
        :param log_channel:
        :param on_message:
        :param on_message_edit:
        :param on_message_delete:
        :param on_reaction_add:
        :param on_member_ban:
        :param on_member_unban:
        :return: nextcord.Embed
        ----------
        """

        embed = CtxEmbed(
            bot=self.bot,
            ctx=ctx,
            color=nextcord.Color.red(),
            description="Metrio | Moderation"
        )

        embed.add_field(
            name="Log channel",
            value=log_channel,
            inline=False
        )
        embed.add_field(
            name="Message log",
            value=on_message
        )
        embed.add_field(
            name="Message edit log",
            value=on_message_edit
        )
        embed.add_field(
            name="Message delete log",
            value=on_message_delete,
            inline=False
        )
        embed.add_field(
            name="Reaction log",
            value=on_reaction_add
        )
        embed.add_field(
            name="Member ban log",
            value=on_member_ban
        )
        embed.add_field(
            name="Member unban log",
            value=on_member_unban
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
                description="The channel you send the log messages."
            ),
            on_message: str = nextcord.SlashOption(
                description="Logs when user send a message",
                choices=["on", "off"]
            ),
            on_message_edit: str = nextcord.SlashOption(
                description="Logs when user edit a message",
                choices=["on", "off"]
            ),
            on_message_delete: str = nextcord.SlashOption(
                description="Logs when user delete a message",
                choices=["on", "off"]
            ),
            on_reaction_add: str = nextcord.SlashOption(
                description="Logs when user add a reaction",
                choices=["on", "off"]
            ),
            on_member_ban: str = nextcord.SlashOption(
                description="Logs when user banned from the server",
                choices=["on", "off"]
            ),
            on_member_unban: str = nextcord.SlashOption(
                description="Logs when user was unbanned from the server",
                choices=["on", "off"]
            )
    ) -> PartialInteractionMessage | WebhookMessage:

        """
        Attributes
        ----------
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
            db_session = SQLSession.create_session()

            logs = LogsTable(
                server_id=ctx.guild.id,
                log_channel_id=log_channel.id,
                on_message=on_message,
                on_message_edit=on_message_edit,
                on_message_delete=on_message_delete,
                on_reaction_add=on_reaction_add,
                on_member_ban=on_member_ban,
                on_member_unban=on_member_unban
            )
            db_session.add(logs)
            db_session.commit()
            db_session.close()
            db_conn.close()

            await settingLogs.set_logs(
                server_id=ctx.guild.id,
                log_channel_id=log_channel.id,
                on_message=on_message,
                on_message_edit=on_message_edit,
                on_message_delete=on_message_delete,
                on_reaction_add=on_reaction_add,
                on_member_ban=on_member_ban,
                on_member_unban=on_member_unban
            )

            embed_setup_logs = await self.create_embed(
                ctx=ctx,
                log_channel=log_channel.name,
                on_message=on_message,
                on_message_edit=on_message_edit,
                on_message_delete=on_message_delete,
                on_reaction_add=on_reaction_add,
                on_member_ban=on_member_ban,
                on_member_unban=on_member_unban
            )

            return await ctx.send(embed=embed_setup_logs, ephemeral=True)

        query = update(LogsTable).values(
            log_channel_id=log_channel.id,
            on_message=on_message,
            on_message_edit=on_message_edit,
            on_message_delete=on_message_delete,
            on_reaction_add=on_reaction_add,
            on_member_ban=on_member_ban,
            on_member_unban=on_member_unban
        ).where(LogsTable.server_id == ctx.guild.id)
        db_conn.execute(query)
        db_conn.commit()
        db_conn.close()

        await settingLogs.set_logs(
            server_id=ctx.guild.id,
            log_channel_id=log_channel.id,
            on_message=on_message,
            on_message_edit=on_message_edit,
            on_message_delete=on_message_delete,
            on_reaction_add=on_reaction_add,
            on_member_ban=on_member_ban,
            on_member_unban=on_member_unban
        )

        embed_setup_logs = await self.create_embed(
            ctx=ctx,
            log_channel=log_channel.name,
            on_message=on_message,
            on_message_edit=on_message_edit,
            on_message_delete=on_message_delete,
            on_reaction_add=on_reaction_add,
            on_member_ban=on_member_ban,
            on_member_unban=on_member_unban
        )

        await ctx.send(embed=embed_setup_logs, ephemeral=True)


def setup(bot):
    bot.add_cog(LogSetup(bot))
