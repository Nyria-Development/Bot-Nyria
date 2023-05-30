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
from nextcord.ext import commands
from src.logger.logger import Logging
from src.services.covert import Convert
from src.loader.translator import GetTranslator
from deep_translator import GoogleTranslator
from src.templates.embeds.messageEmbed import MessageEmbed


class TranslateReaction(commands.Cog):
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

        supported_languages = GetTranslator().get_reaction_language()[0]
        key: str = await Convert.convert_to_byte(str(payload.emoji))
        user = payload.member

        try:
            language = supported_languages[key]
        except KeyError:
            return

        guild = self.bot.get_guild(payload.guild_id)
        Logging().info(f"Listener :: translate-reaction :: {guild} :: {payload.member}")

        channel = self.bot.get_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)

        translated_message = GoogleTranslator(
            target=language
        ).translate(text=message.content)

        embed_translation = MessageEmbed(
            bot=self.bot,
            message=message,
            color=nextcord.Color.orange(),
            description="Fun | Diasio"
        )
        embed_translation.add_field(
            name="Translation",
            value=translated_message
        )
        await user.send(embed=embed_translation)


def setup(bot):
    bot.add_cog(TranslateReaction(bot))
