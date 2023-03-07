import nextcord
from nextcord.ext import commands
import random


from src.templates import embeds


class messages(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot == False:
            print(message.content)
            log_channel = self.bot.get_channel(1082632691196903424)
            log_embed = nextcord.Embed(title="",
                                     description=f"Eine neue Nachricht wurde von {message.author.mention} in {message.channel.mention} verfasst",
                                     color=0x081e8c)
            await log_channel.send(embed=log_embed)

    @commands.Cog.listener()
    async def on_message_delete(self, message: str):
        print(message)

    @commands.Cog.listener()
    async def on_message_edit(self, message: str):
        print(message)



def setup(bot):
    bot.add_cog(messages(bot))
