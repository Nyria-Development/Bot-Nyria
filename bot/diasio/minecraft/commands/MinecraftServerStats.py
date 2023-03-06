import nextcord
from nextcord.ext import commands
from src.loader.jsonLoader import Diasio
from mcstatus import JavaServer, BedrockServer
from src.templates import embeds


class MinecraftServerStats(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(
        name="diasio-minecraft-server-stats",
        description="Show minecraft server stats.",
        force_global=True
    )
    async def minecraft_server_stats(self, ctx: nextcord.Interaction, server_name: str, server_type=nextcord.SlashOption(choices=Diasio().get_minecraft_server_types()), port: int = None):
        embed_minecraft_server = embeds.TemplateEmbed(
            bot=self.bot,
            ctx=ctx,
            description="Fun | Diasio",
            color=nextcord.Color.orange()
        )

        if server_type == "java":
            java_server = JavaServer.lookup(f"{server_name.rstrip()}:{port if port is not None else 25565 or port if port is None else port}")

            try:
                status = java_server.status()
            except (TimeoutError, OSError):
                return await ctx.send("The network blocks the request or not exist.", ephemeral=True)

            player_online = status.players.online
            latency = java_server.ping()

            embed_minecraft_server.add_field(name="Online Players", value=player_online)
            embed_minecraft_server.add_field(name="Latency", value=latency)

            return await ctx.send(embed=embed_minecraft_server, ephemeral=True)

        bedrock_server = BedrockServer.lookup(f"{server_name.rstrip()}:{port if port is not None else 19132 or port if port is None else port}")
        try:
            status = bedrock_server.status()
        except (TimeoutError, OSError):
            return await ctx.send("The network blocks the request or not exist.", ephemeral=True)

        player_online = status.players_online
        latency = status.latency

        embed_minecraft_server.add_field(name="Online Players", value=player_online)
        embed_minecraft_server.add_field(name="Latency", value=latency)

        await ctx.send(embed=embed_minecraft_server, ephemeral=True)


def setup(bot):
    bot.add_cog(MinecraftServerStats(bot))
