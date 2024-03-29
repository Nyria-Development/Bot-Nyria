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
from src.settings.voice import permissions


class VoiceRename(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(
        name="kanio-voice-rename",
        description="Change the name from the voice.",
        force_global=True,
    )
    async def voice_rename(
            self,
            ctx: nextcord.Interaction,
            voice_name: str = nextcord.SlashOption(
                description="The name for the new voice name.",
                required=True
            )
    ) -> PartialInteractionMessage | WebhookMessage:

        """
        Attributes
        ----------
        :param ctx:
        :param voice_name:
        :return: None
        ----------
        """

        Logging().info(f"Command :: kanio-voice-rename :: {ctx.guild.name} :: {ctx.user}")

        if not await permissions.check(ctx):
            return await ctx.send("You have no permission to do that.", ephemeral=True)

        if len(voice_name) > 25:
            return await ctx.send("The new channel name is to long.", ephemeral=True)

        await ctx.user.voice.channel.edit(
            name=f"{voice_name}-VC"
        )
        await ctx.send(f"The channel name was changed to **{voice_name}-VC**")


def setup(bot):
    bot.add_cog(VoiceRename(bot))
