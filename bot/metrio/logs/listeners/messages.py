import nextcord
from nextcord.ext import commands
from src.settings.logs import settingLogs
from src.templates.embeds.logEmbed import LogEmbed


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

        logs = settingLogs.get_logs_on_off(
            guild_id=message.guild.id
        )

        if not logs or logs["on_message"] == "off":
            return

        log_channel = self.bot.get_channel(logs["log_channel_id"])
        embed_on_message = LogEmbed(
            bot=self.bot,
            user=message.author,
            title="Message | NewMessage",
            description=f"{message.author.mention} | {message.channel.mention}"
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

        logs = settingLogs.get_logs_on_off(
            guild_id=before.guild.id
        )
        if logs is False:
            return

        if logs["on_message_edit"] == "off":
            return

        log_channel = self.bot.get_channel(logs["log_channel_id"])
        embed_on_message = LogEmbed(
            bot=self.bot,
            user=after.author,
            title="Message | MessageEdit",
            description=f"{after.author.mention} | {after.channel.mention}"
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

        logs = settingLogs.get_logs_on_off(
            guild_id=message.guild.id
        )
        if logs is False:
            return

        if logs["on_message_delete"] == "off":
            return

        log_channel = self.bot.get_channel(logs["log_channel_id"])
        embed_on_message = LogEmbed(
            bot=self.bot,
            user=message.author,
            title="Message | MessageEdit",
            description=f"{message.author.mention} | {message.channel.mention}"
        )

        if message.content:
            embed_on_message.add_field(
                name="Message deleted",
                value=message.content
            )
        await log_channel.send(embed=embed_on_message)


def setup(bot):
    bot.add_cog(Messages(bot))
