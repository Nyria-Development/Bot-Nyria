import nextcord
from nextcord.ext import commands
from src.settings.logs import settingLogs
from src.templates.embeds.payloadEmbed import PayloadEmbed


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

        logs = await settingLogs.get_logs(
            guild_id=payload.guild_id
        )
        if logs is False:
            return

        if logs["on_message"] == "off":
            return

        log_channel = self.bot.get_channel(logs["log_channel_id"])

        embed_on_reaction_add = PayloadEmbed(
            bot=self.bot,
            payload=payload,
            color=nextcord.Color.red(),
            description="Metrio | Moderation"
        )
        embed_on_reaction_add.add_field(
            name="Reaction",
            value=payload.emoji
        )

        await log_channel.send(embed=embed_on_reaction_add)


def setup(bot):
    bot.add_cog(LogReaction(bot))
