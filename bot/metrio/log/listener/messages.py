import nextcord
from nextcord.ext import commands
from src.loader.jsonLoader import Metrio


class Messages(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: nextcord.Message):
        if not message.author.bot:
            print(message.content)
            for guild in Metrio().get_guilds():
                if guild['log_channel_id'] == message.guild.id:
                    #sucht die rightige Guilde raus...
                    print(guild)
            log_channel = self.bot.get_channel(1082632691196903424) #hier wird dann die ID für die Guilde hineingefügt
            log_embed = nextcord.Embed(title="New message",
                                       description=f"A new message from {message.author.mention} was send to {message.channel.mention}.",
                                       color=0x081e8c)
            if message.content:
                log_embed.add_field(name="Content", value=message.content)
            await log_channel.send(embed=log_embed)

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        print(message.content)
        log_channel = self.bot.get_channel(1082632691196903424)
        log_embed = nextcord.Embed(title="Message was deleted",
                                   description=f"A message by {message.author.mention} was deleted in {message.channel.mention}.",
                                   color=0x081e8c)
        if message.content:
            log_embed.add_field(name="Content", value=message.content)
        await log_channel.send(embed=log_embed)

    @commands.Cog.listener()
    async def on_message_edit(self, befor, after):
        print(befor.content, after.content)
        log_channel = self.bot.get_channel(1082632691196903424)
        log_embed = nextcord.Embed(title="Message was edited",
                                   description=f"A message from {befor.author.mention} was edited in {befor.channel.mention}.",
                                   color=0x081e8c)
        if befor.content:
            log_embed.add_field(name="befor Content", value=befor.content)
        if after.content:
            log_embed.add_field(name="after Content", value=after.content)
        await log_channel.send(embed=log_embed)


def setup(bot):
    bot.add_cog(Messages(bot))
