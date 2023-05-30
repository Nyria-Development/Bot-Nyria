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
from deep_translator import GoogleTranslator
from src.loader.translator import GetTranslator
from src.logger.logger import Logging


class TranslateToLanguage(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(
        name="diasio-translator-translate",
        description="Translate any to text to some languages.",
        force_global=True
    )
    async def translate(
            self,
            ctx: nextcord.Interaction,
            language: str = nextcord.SlashOption(
                description="The language you want to translate.",
                choices=GetTranslator().get_supported_languages()[0],
                required=True
            ),
            text: str = nextcord.SlashOption(
                description="The text you want to translate",
                required=True
            )
    ) -> None:

        """
        Attributes
        ----------
        :param ctx:
        :param language:
        :param text:
        :return: None
        ----------
        """

        Logging().info(f"Command :: diasio-translator-translate :: {ctx.guild.name} :: {ctx.user}")

        translated_text = GoogleTranslator(
            target=language
        ).translate(text)

        await ctx.send(translated_text, ephemeral=True)


def setup(bot):
    bot.add_cog(TranslateToLanguage(bot))
