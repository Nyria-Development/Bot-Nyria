import nextcord
from nextcord.ext import commands
from src.settings.logs import settingLogs
from src.templates.embeds.logEmbed import LogEmbed


class LogReaction(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_raw_reaction_add(
            self,
            payload: nextcord.RawReactionActionEvent
    ) -> None:

        """
        Attributes
        ----------
        :param payload:
        :return: None
        ----------
        """

        if payload.member.bot:
            return

        logs = settingLogs.get_logs_on_off(
            guild_id=payload.guild_id
        )
        if logs is False:
            return

        if logs["on_reaction_add"] == "off":
            return

        log_channel = self.bot.get_channel(logs["log_channel_id"])
        payload_user = self.bot.get_user(payload.user_id)
        payload_message = await self.bot.get_channel(payload.channel_id).fetch_message(payload.message_id)
        embed_on_reaction_add = LogEmbed(
            bot=self.bot,
            user=payload_user,
            title="Reaction | Add",
            description=f"{payload_user.mention} | {payload_message.jump_url}"
        )
        embed_on_reaction_add.add_field(
            name="Reaction",
            value=payload.emoji
        )

        await log_channel.send(embed=embed_on_reaction_add)

    @commands.Cog.listener()
    async def on_raw_reaction_remove(
            self,
            payload: nextcord.RawReactionActionEvent
    ) -> None:

        """
        Attributes
        ----------
        :param payload:
        :return: None
        ----------
        """

        logs = settingLogs.get_logs_on_off(
            guild_id=payload.guild_id
        )

        if logs["on_reaction_remove"] == "off" or not logs:
            return

        log_channel = self.bot.get_channel(logs["log_channel_id"])
        payload_user = self.bot.get_user(payload.user_id)
        payload_message = await self.bot.get_channel(payload.channel_id).fetch_message(payload.message_id)
        embed_on_reaction_remove = LogEmbed(
            bot=self.bot,
            user=payload_user,
            title="Reaction | Remove",
            description=f"{payload_user.mention} | {payload_message.jump_url}"
        )
        embed_on_reaction_remove.add_field(
            name="Reaction",
            value=payload.emoji
        )

        await log_channel.send(embed=embed_on_reaction_remove)


def setup(bot):
    bot.add_cog(LogReaction(bot))
