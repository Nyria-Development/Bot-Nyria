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

from src.logger.logger import Logging
from sqlalchemy import select
from src.database.core.engine import SQLEngine
from src.database.tables.setup import LogsTable
from src.settings.logs import settingLogs


async def logs_memory_cache():
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
            log_config_int=log[3]
        )
    Logging().info("All logs in cache")


def setup(bot):
    pass
