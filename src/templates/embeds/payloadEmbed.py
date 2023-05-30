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


class PayloadEmbed(nextcord.Embed):
    def __init__(self, bot: commands.Bot, payload: nextcord.RawReactionActionEvent, color: nextcord.Color, description: str = ""):
        super().__init__()
        self.bot = bot
        self.payload = payload
        self.color = color
        self.description = description

        self.title = self.bot.user.name
        self.set_thumbnail(url=self.bot.user.avatar)
        self.set_footer(text=f"Created by {self.bot.user.name} | {datetime.date.today()}")
        self.set_author(name=self.payload.member.name, icon_url=self.payload.member.avatar)
