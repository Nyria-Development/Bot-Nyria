import nextcord
from nextcord.ext import commands
from src.logger.logger import Logging
from sqlalchemy import select
from src.database.tables.setup import VoiceTable
from src.database.core.engine import SQLEngine
from src.settings.voice import settingVoice


class StartupVoiceCleaner(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        Logging().info("Clean all voices")

        db_conn = SQLEngine.engine.connect()
        query = select(VoiceTable)

        voices = db_conn.execute(query).all()
        if not voices:
            return

        for voice in voices:
            guild = self.bot.get_guild(voice[1])
            category = nextcord.utils.get(guild.categories, name=voice[2])

            await settingVoice.set_category(
                guild_id=guild.id,
                category_name=voice[2]
            )

            if len(category.channels) == 1:
                continue

            for channel in category.channels:
                if str(channel) == "Create Voice":
                    continue

                await channel.delete()

        db_conn.close()


def setup(bot):
    bot.add_cog(StartupVoiceCleaner(bot))
