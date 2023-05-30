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

import nextcord
from nextcord import PartialInteractionMessage, WebhookMessage
from nextcord.ext import commands
from src.logger.logger import Logging
from src.settings.voice import permissions, settingVoice
from src.templates.embeds.ctxEmbed import CtxEmbed


class VoiceCurrentSettings(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(
        name="kanio-voice-current-settings",
        description="Show the current voice settings.",
        force_global=True
    )
    async def voice_current_settings(
            self,
            ctx: nextcord.Interaction,
            voice: nextcord.VoiceChannel = nextcord.SlashOption(
                description="The voice that you want to see the settings.",
                required=True
            )
    ) -> PartialInteractionMessage | WebhookMessage:

        """
        Attributes
        ----------
        :param ctx:
        :param voice:
        :return:
        ----------
        """

        Logging().info(f"Command :: kanio-voice-current-settings :: {ctx.guild.name} :: {ctx.user}")

        category_name = await settingVoice.get_category(
            guild_id=ctx.guild.id
        )
        if category_name is None:
            return await ctx.send("The voice system is currently not active.", ephemeral=True)

        category = nextcord.utils.get(ctx.guild.categories, name=category_name.lower())

        if voice not in category.channels:
            return await ctx.send(f"Please select a channel in **{category.name}**", ephemeral=True)

        if voice.name.lower() == "create voice":
            return await ctx.send("Please select a user channel not a system channel.", ephemeral=True)

        host = await permissions.get_host(
            channel_id=ctx.user.voice.channel.id
        )

        embed_voice_settings = CtxEmbed(
            bot=self.bot,
            ctx=ctx,
            color=nextcord.Color.blurple(),
            description="kanio | Channel"
        )
        embed_voice_settings.add_field(
            name="Host",
            value=host
        )
        embed_voice_settings.add_field(
            name="Aktive users",
            value=len(voice.members)
        )
        embed_voice_settings.add_field(
            name="Limit",
            value=voice.user_limit
        )

        await ctx.send(embed=embed_voice_settings, ephemeral=True)


def setup(bot):
    bot.add_cog(VoiceCurrentSettings(bot))
