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
