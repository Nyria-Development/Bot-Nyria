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
from src.templates.embeds.ctxEmbed import CtxEmbed
from mcstatus import JavaServer, BedrockServer


class MinecraftServerStatus(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(
        name="diasio-minecraft-server-stats",
        description="Show minecraft server stats of any server.",
        force_global=True
    )
    async def minecraft_server_stats(
            self,
            ctx: nextcord.Interaction,
            ip_address: str = nextcord.SlashOption(
                description="The Ip address or domain of the server."
            ),
            server_type: str = nextcord.SlashOption(
                description="Choose the type of the server.",
                choices=["java", "bedrock"]
            ),
            port: int = nextcord.SlashOption(
                description="Have your server a custom port?",
                required=False
            )
    ) -> PartialInteractionMessage | WebhookMessage:

        """
        Attributes
        ----------
        :param ctx:
        :param ip_address:
        :param server_type:
        :param port:
        :return: None
        ----------
        """

        Logging().info(f"Command :: diasio-minecraft-server-stats :: {ctx.guild.name} :: {ctx.user}")

        embed_minecraft_server_stats = CtxEmbed(
            bot=self.bot,
            ctx=ctx,
            color=nextcord.Color.orange(),
            description="Fun | Diasio"
        )

        if server_type == "java":
            java_server = JavaServer.lookup(f"{ip_address.rstrip()}:{port if port is not None else 25565 or port if port is None else port}")

            try:
                status = java_server.status()
            except (TimeoutError, OSError):
                return await ctx.send("The network blocks the request or not exist.", ephemeral=True)

            player_online = status.players.online
            latency = java_server.ping()

            embed_minecraft_server_stats.add_field(
                name="Server name",
                value=ip_address,
                inline=False
            )
            embed_minecraft_server_stats.add_field(
                name="Online Players",
                value=player_online
            )
            embed_minecraft_server_stats.add_field(
                name="Latency",
                value=f"{round(latency)}ms"
            )

            return await ctx.send(embed=embed_minecraft_server_stats, ephemeral=True)

        bedrock_server = BedrockServer.lookup(f"{ip_address.rstrip()}:{port if port is not None else 19132 or port if port is None else port}")
        try:
            status = bedrock_server.status()
        except (TimeoutError, OSError):
            return await ctx.send("The network blocks the request or not exist.", ephemeral=True)

        player_online = status.players_online
        latency = status.latency

        embed_minecraft_server_stats.add_field(
            name="Server name",
            value=ip_address,
            inline=False
        )
        embed_minecraft_server_stats.add_field(
            name="Online Players",
            value=player_online
        )
        embed_minecraft_server_stats.add_field(
            name="Latency",
            value=f"{round(latency)}ms"
        )

        await ctx.send(embed=embed_minecraft_server_stats, ephemeral=True)


def setup(bot):
    bot.add_cog(MinecraftServerStatus(bot))
