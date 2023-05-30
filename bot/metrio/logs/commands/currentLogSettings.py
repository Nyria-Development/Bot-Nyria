# All Rights Reserved
# Copyright (c) 2023 Nyria
#
# This code, including all accompanying software, documentation, and related materials, is the exclusive property
# of Nyria. All rights are reserved.
#
# Any use, reproduction, distribution, or modification of the code without the express written
# permission of Nyria is strictly prohibited.
#
# No warranty is provided for the code, and Nyria shall not be liable for any claims, damages,
# or other liability arising from the use or inability to use the code.

from typing import Union

import nextcord
from nextcord import PartialInteractionMessage, WebhookMessage
from nextcord.ext import commands
from src.logger.logger import Logging
from src.settings.logs import settingLogs
from src.templates.embeds.ctxEmbed import CtxEmbed


class CurrentLogSetting(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.config_list = settingLogs.config_log_list

    @nextcord.slash_command(
        name="metrio-log-current-settings",
        description="Show the current log settings",
        force_global=True,
        default_member_permissions=8
    )
    async def log_current_settings(
            self,
            ctx: nextcord.Interaction
    ) -> Union[PartialInteractionMessage, WebhookMessage]:

        """
        Attributes
        ----------
        :param ctx:
        :return: None
        ----------
        """

        Logging().info(f"Command :: metrio-log-current-settings :: {ctx.guild.name} :: {ctx.user}")

        logs = settingLogs.get_logs_on_off(
            guild_id=ctx.guild.id
        )
        if logs is False:
            return await ctx.send("The log system is not available on this server.", ephemeral=True)

        embed_current_setting_logs = CtxEmbed(
            bot=self.bot,
            ctx=ctx,
            color=nextcord.Color.red(),
            description="Metrio | Moderation"
        )

        log_channel = self.bot.get_channel(logs["log_channel_id"])
        embed_current_setting_logs.add_field(
            name="Log channel",
            value=log_channel.mention,
            inline=False
        )
        for config in self.config_list:
            embed_current_setting_logs.add_field(
                name=" ".join(config.split("_")),
                value=logs[config]
            )

        await ctx.send(embed=embed_current_setting_logs, ephemeral=True)


def setup(bot):
    bot.add_cog(CurrentLogSetting(bot))
