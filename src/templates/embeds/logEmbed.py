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
import datetime
from nextcord.ext import commands


class LogEmbed(nextcord.Embed):
    def __init__(self, bot: commands.Bot, user: nextcord.User, title: str = "Log | Nyria", description: str = ""):
        super().__init__()
        self.bot = bot
        self.user = user
        self.color = 0x151642
        self.title = title
        self.description = description

        self.set_footer(text=f"Created by {self.bot.user.name} | {datetime.date.today()}")
