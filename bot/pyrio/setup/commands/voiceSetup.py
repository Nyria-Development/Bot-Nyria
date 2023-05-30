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
from src.settings.voice import settingVoice
from src.database.core.engine import SQLEngine
from src.database.core.session import SQLSession
from src.database.tables.setup import VoiceTable
from sqlalchemy import select, update


class VoiceSetup(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @staticmethod
    async def create_voices(
            ctx: nextcord.Interaction,
            category_name: str
    ) -> None:

        """
        Attributes
        ----------
        :param ctx:
        :param category_name:
        :return: None
        ----------
        """

        category = await ctx.guild.create_category(
            name=category_name.lower()
        )
        await ctx.guild.create_voice_channel(
            name="Create Voice",
            category=category
        )

    @nextcord.slash_command(
        name="pyrio-setup-voice",
        description="Setup the voice system.",
        force_global=True,
        default_member_permissions=8
    )
    async def voice_setup(
            self,
            ctx: nextcord.Interaction,
            category_name: str = nextcord.SlashOption(
                description="Enter a name for your voice category",
                required=True
            )
    ) -> PartialInteractionMessage | WebhookMessage:

        """
        Attributes
        ----------
        :param ctx:
        :param category_name:
        :return: PartialInteractionMessage | WebhookMessage
        ----------
        """

        Logging().info(f"Command :: pyrio-setup-voice :: {ctx.guild.name} :: {ctx.user}")

        if len(category_name) > 30:
            return await ctx.send("The name of the category is to long.", ephemeral=True)

        db_conn = SQLEngine.engine.connect()

        query = select(VoiceTable).where(VoiceTable.server_id == ctx.guild.id)
        selected_category = db_conn.execute(query).all()

        if not selected_category:
            db_session = SQLSession.create_session()

            selected_category = VoiceTable(
                server_id=ctx.guild.id,
                category_name=category_name.lower()
            )

            db_session.add(selected_category)
            db_session.commit()
            db_session.close()
            db_conn.close()

            await settingVoice.set_category(
                guild_id=ctx.guild.id,
                category_name=category_name.lower()
            )
            await self.create_voices(
                ctx=ctx,
                category_name=category_name
            )

            return await ctx.send(f"Category set to **{category_name.lower()}**", ephemeral=True)

        query = update(VoiceTable).values(category_name=category_name.lower()).where(VoiceTable.server_id == ctx.guild.id)
        db_conn.execute(query)
        db_conn.commit()
        db_conn.close()

        await settingVoice.set_category(
            guild_id=ctx.guild.id,
            category_name=category_name
        )

        await self.create_voices(
            ctx=ctx,
            category_name=category_name
        )

        old_category = nextcord.utils.get(ctx.guild.categories, name=selected_category[0][2])
        for channel in old_category.channels:
            await channel.delete()

        await old_category.delete()

        await ctx.send(f"Category updated to: **{category_name.lower()}**", ephemeral=True)


def setup(bot):
    bot.add_cog(VoiceSetup(bot))
