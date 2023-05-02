from nextcord.ext import commands
from src.logger.logger import Logging
from sqlalchemy import select
from src.database.core.engine import SQLEngine
from src.database.tables.setup import LogsTable
from src.settings.logs import settingLogs


class LogsMemoryCache(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        db_conn = SQLEngine.engine.connect()

        query = select(LogsTable)
        logs = db_conn.execute(query).all()

        if not logs:
            Logging().info("No logs to load in cache")
            return

        for log in logs:
            await settingLogs.set_logs(
                server_id=log[1],
                log_channel_id=log[2],
                on_message=log[3],
                on_message_edit=log[4],
                on_message_delete=log[5],
                on_reaction_add=log[6],
                on_member_ban=log[7],
                on_member_unban=log[8]
            )
        Logging().info("All logs in cache")


def setup(bot):
    bot.add_cog(LogsMemoryCache(bot))
