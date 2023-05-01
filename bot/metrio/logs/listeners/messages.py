import nextcord
from nextcord.ext import commands
from src.settings.logs import settingLogs
from src.templates.embeds.messageEmbed import MessageEmbed


class Messages(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(
            self,
            message: nextcord.Message
    ) -> None:

        """
        Attributes
        ----------
        :param message:
        :return: None
        ----------
        """

        if message.author.bot:
            return

        logs = await settingLogs.get_logs(
            guild_id=message.guild.id
        )
        if logs is False:
            return

        if logs["on_message"] == "off":
            return

        log_channel = self.bot.get_channel(logs["log_channel_id"])
        embed_on_message = MessageEmbed(
            bot=self.bot,
            message=message,
            color=nextcord.Color.red(),
            description="Metrio | Moderation"
        )

        if message.content:
            embed_on_message.add_field(
                name="Content",
                value=message.content
            )
        if message.attachments:
            embed_on_message.add_field(
                name="Attachments",
                value=message.attachments
            )
        await log_channel.send(embed=embed_on_message)

    @commands.Cog.listener()
    async def on_message_edit(
            self,
            before: nextcord.Message,
            after: nextcord.Message
    ) -> None:

        """
        Attributes
        ----------
        :param before
        :param after
        :return: None
        ----------
        """

        if before.author.bot:
            return

        logs = await settingLogs.get_logs(
            guild_id=before.guild.id
        )
        if logs is False:
            return

        if logs["on_message_edit"] == "off":
            return

        log_channel = self.bot.get_channel(logs["log_channel_id"])
        embed_on_message = MessageEmbed(
            bot=self.bot,
            message=before,
            color=nextcord.Color.red(),
            description="Metrio | Moderation"
        )

        if before.content:
            embed_on_message.add_field(
                name="Content before",
                value=before.content,
                inline=False
            )
            embed_on_message.add_field(
                name="Content after",
                value=after.content
            )
        await log_channel.send(embed=embed_on_message)

    @commands.Cog.listener()
    async def on_message_delete(
            self,
            message: nextcord.Message
    ) -> None:

        """
        Attributes
        ----------
        :param message:
        :return: None
        ----------
        """

        if message.author.bot:
            return

        logs = await settingLogs.get_logs(
            guild_id=message.guild.id
        )
        if logs is False:
            return

        if logs["on_message_delete"] == "off":
            return

        log_channel = self.bot.get_channel(logs["log_channel_id"])
        embed_on_message = MessageEmbed(
            bot=self.bot,
            message=message,
            color=nextcord.Color.red(),
            description="Metrio | Moderation"
        )

        if message.content:
            embed_on_message.add_field(
                name="Message deleted",
                value=message.content
            )
        await log_channel.send(embed=embed_on_message)


def setup(bot):
    bot.add_cog(Messages(bot))
