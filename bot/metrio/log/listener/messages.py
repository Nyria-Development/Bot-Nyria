import nextcord
from nextcord.ext import commands
from src.dictionaries import logs
from src.templates import embeds


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

        log_embed = embeds.MessageEmbed(
            bot=self.bot,
            message=message,
            description="Moderation | Metrio",
            color=nextcord.Color.blue()
        )
        log_embed.add_field(name="Channel", value=message.channel)
        log_embed.add_field(name="New Message", value=message.content)
        await log_channel.send(embed=log_embed)

    @commands.Cog.listener()
    async def on_message_delete(self, message: nextcord.Message) -> None:
        log_channel = self.bot.get_channel(logs.get_log_channel(server_id=message.guild.id))

        if log_channel is None:
            return

        log_embed = embeds.MessageEmbed(
            bot=self.bot,
            message=message,
            description="Moderation | Metrio",
            color=nextcord.Color.blue()
        )
        log_embed.add_field(name="Channel", value=message.channel)
        log_embed.add_field(name="Message deleted", value=message.content)
        await log_channel.send(embed=log_embed)

    @commands.Cog.listener()
    async def on_message_edit(self, before: nextcord.Message, after: nextcord.Message) -> None:
        log_channel = self.bot.get_channel(logs.get_log_channel(server_id=after.guild.id))

        if log_channel is None:
            return

        log_embed = embeds.MessageEmbed(
            bot=self.bot,
            message=after,
            description="Moderation | Metrio",
            color=nextcord.Color.blue()
        )
        log_embed.add_field(name="before Content", value=before.content)
        log_embed.add_field(name="after Content", value=after.content)

        await log_channel.send(embed=log_embed)


def setup(bot):
    bot.add_cog(Messages(bot))
