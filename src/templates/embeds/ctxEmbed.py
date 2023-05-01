import nextcord
import datetime
from nextcord import Embed
from nextcord.ext import commands


class CtxEmbed(Embed):
    def __init__(self, bot: commands.Bot, ctx: nextcord.Interaction, color: nextcord.Color, description=""):
        super().__init__()
        self.bot = bot
        self.ctx = ctx
        self.color = color
        self.description = description

        self.title = self.bot.user.name
        self.set_thumbnail(url=self.bot.user.avatar)
        self.set_footer(text=f"Created by {self.bot.user.name} | {datetime.date.today()}")
        self.set_author(name=self.ctx.user.name, icon_url=self.ctx.user.avatar)
