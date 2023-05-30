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
import asyncio
from nextcord.ext import commands, tasks
from src.logger.logger import Logging


class Status(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # Show the status in discord
    @tasks.loop(seconds=30)
    async def status(self):
        await self.bot.change_presence(
            activity=nextcord.Game("Imagination is way more important than knowledge."),
            status=nextcord.Status.do_not_disturb
        )
        await asyncio.sleep(15)
        await self.bot.change_presence(
            activity=nextcord.Game(f"Nyria supports {len(self.bot.guilds)} Server."),
            status=nextcord.Status.do_not_disturb
        )

    # start the status
    @commands.Cog.listener()
    async def on_ready(self):
        self.status.start()
        Logging().info("Status started")


def setup(bot):
    bot.add_cog(Status(bot))
