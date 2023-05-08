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
