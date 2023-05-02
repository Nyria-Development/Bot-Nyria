import nextcord
import datetime
from nextcord.ext import commands


class StandAloneEmbed(nextcord.Embed):
    def __init__(self, bot: commands.Bot, color: nextcord.Color, description: str = ""):
        super().__init__()
        self.bot = bot
        self.color = color
        self.description = description

        self.title = self.bot.user.name
        self.set_thumbnail(url=self.bot.user.avatar)
        self.set_footer(text=f"Created by {self.bot.user.name} | {datetime.date.today()}")
