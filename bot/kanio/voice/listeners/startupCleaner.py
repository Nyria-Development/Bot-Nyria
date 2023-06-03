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
from src.logger.logger import Logging
from sqlalchemy import select
from src.database.tables.setup import VoiceTable
from src.database.core.engine import SQLEngine
from src.settings.voice import settingVoice


async def startup_voice_cleaner(bot):
    Logging().info("Clean all voices")

    db_conn = SQLEngine.engine.connect()
    query = select(VoiceTable)

    voices = db_conn.execute(query).all()
    if not voices:
        return

    for voice in voices:
        guild = bot.get_guild(voice[1])
        category = nextcord.utils.get(guild.categories, name=voice[2])

        await settingVoice.set_category(
            guild_id=guild.id,
            category_name=voice[2]
        )

        if len(category.channels) == 1:
            continue

        for channel in category.channels:
            if str(channel) == "Create Voice":
                continue

            await channel.delete()

    db_conn.close()


def setup(bot):
    pass
