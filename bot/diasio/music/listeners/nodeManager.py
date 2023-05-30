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

import mafic
from nextcord.ext import commands
from src.logger.logger import Logging
from src.loader.logins import GetLogin


class MusicNodeManager(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.pool = mafic.NodePool(self.bot)

        self.loop = self.bot.loop.create_task(self.register_node())

    async def register_node(self):
        host, port, password = GetLogin().get_lavalink()

        await self.pool.create_node(
            host=host,
            port=port,
            label="MAIN",
            password=password
        )
        Logging().info("Music Node connected")


def setup(bot):
    bot.add_cog(MusicNodeManager(bot))
