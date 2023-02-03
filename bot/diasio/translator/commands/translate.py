import deep_translator.exceptions
import nextcord
from nextcord.ext import commands
from deep_translator import GoogleTranslator


class Translate(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(
        name="diasio-translate",
        description="Translate any text in the most languages.",
        force_global=True
    )
    async def translate(self, ctx: nextcord.Interaction, text: str, language: str):
        try:
            translator = GoogleTranslator(target=language)
        except deep_translator.exceptions.LanguageNotSupportedException:
            return await ctx.send("Language not supported.", ephemeral=True)

        translated_text = translator.translate(text=text)
        await ctx.send(translated_text, ephemeral=True)


def setup(bot):
    bot.add_cog(Translate(bot))
