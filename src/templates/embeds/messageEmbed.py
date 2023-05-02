import nextcord
import datetime
from nextcord.ext import commands


class MessageEmbed(nextcord.Embed):
    def __init__(self, bot: commands.Bot, message: nextcord.Message, color: nextcord.Color, description: str = ""):
        super().__init__()
        self.bot = bot
        self.message = message
        self.color = color
        self.description = description

        self.title = self.bot.user.name
        self.set_thumbnail(url=self.bot.user.avatar)
        self.set_footer(text=f"Created by {self.bot.user.name} | {datetime.date.today()}")
        self.set_author(name=self.message.author.name, icon_url=self.message.author.avatar)
