import nextcord
from nextcord.ext import commands


class Messages(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: nextcord.Message):
        if not message.author.bot:
            log_channel = self.bot.get_channel(1082632691196903424)

            log_embed = nextcord.Embed(
                title="New message",
                description=f"A new message from {message.author.mention} was send to {message.channel.mention}.",
                color=0x081e8c
            )
            await log_channel.send(embed=log_embed)

    @commands.Cog.listener()
    async def on_message_delete(self, message: str):
        print(message)

    @commands.Cog.listener()
    async def on_message_edit(self, message: str):
        print(message)


def setup(bot):
    bot.add_cog(Messages(bot))
