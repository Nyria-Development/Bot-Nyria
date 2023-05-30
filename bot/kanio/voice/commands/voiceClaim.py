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


class VoiceClaim(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(
        name="kanio-voice-claim",
        description="Claim a voice",
        force_global=True,
        default_member_permissions=8
    )
    async def voice_claim(
            self,
            ctx: nextcord.Interaction,
            voice: nextcord.VoiceChannel = nextcord.SlashOption(
                description="The channel that you want claim",
                required=True
            )
    ) -> None | PartialInteractionMessage | WebhookMessage:

        """
        Attributes
        ----------
        :param ctx:
        :param voice:
        :return: None
        ----------
        """

        Logging().info(f"Command :: kanio-voice-claim :: {ctx.guild.name} :: {ctx.user}")

        category_name = await settingVoice.get_category(
            guild_id=ctx.guild.id
        )
        if category_name is None:
            return await ctx.send("The voice system is currently not active.", ephemeral=True)

        category = nextcord.utils.get(ctx.guild.categories, name=category_name.lower())

        if voice not in category.channels:
            return await ctx.send(f"The selected voice is not in the category **{category.name}**")

        await permissions.change_host(
            channel_id=voice.id,
            member=ctx.user
        )
        await ctx.send("You have claimed the channel.", ephemeral=True)


def setup(bot):
    bot.add_cog(VoiceClaim(bot))
