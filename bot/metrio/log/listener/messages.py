import nextcord
from nextcord.ext import commands
from src.dictionarys import logs


class Messages(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: nextcord.Message) -> None:
        if message.author.bot:
            return

        log_channel = self.bot.get_channel(logs.get_log_channel(server_id=message.guild.id))

        if log_channel is None:
            return

        log_embed = nextcord.Embed(
            title="New message",
            description=f"A new message from {message.author.mention} was send to {message.channel.mention}.",
            color=0x081e8c
        )
        await log_channel.send(embed=log_embed)

    @commands.Cog.listener()
    async def on_message_delete(self, message: nextcord.Message) -> None:
        log_channel = self.bot.get_channel(logs.get_log_channel(server_id=message.guild.id))

        if log_channel is None:
            return

        log_embed = nextcord.Embed(
            title="Message was deleted",
            description=f"A message by {message.author.mention} was deleted in {message.channel.mention}.",
            color=0x081e8c
        )
        await log_channel.send(embed=log_embed)

    @commands.Cog.listener()
    async def on_message_edit(self, before: nextcord.Message, after: nextcord.Message) -> None:
        log_channel = self.bot.get_channel(logs.get_log_channel(server_id=after.guild.id))

        if log_channel is None:
            return

        log_embed = nextcord.Embed(
            title="Message was edited",
            description=f"A message from {before.author.mention} was edited in {before.channel.mention}.",
            color=0x081e8c
        )

        if before.content:
            log_embed.add_field(name="before Content", value=before.content)

        if after.content:
            log_embed.add_field(name="after Content", value=after.content)

        await log_channel.send(embed=log_embed)


def setup(bot):
    bot.add_cog(Messages(bot))
