import nextcord
from nextcord.ext import commands
from src.loader.jsonLoader import Setup
from database.query import Query


class WelcomeSetup(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.database = Query(
            pool_name="welcome_setup",
            pool_size=3
        )

    @nextcord.slash_command(
        name="pyrio-setup-welcome",
        description="Setup any feature from Nyria.",
        force_global=True,
        default_member_permissions=8
    )
    async def setup_welcome(self,
                            ctx: nextcord.Interaction,
                            channel: nextcord.TextChannel,
                            activate=nextcord.SlashOption(choices=Setup().get_activations())
                            ):
        if activate == "no":
            channel_id = self.database.execute(
                query="SELECT channelId FROM welcome WHERE serverId=%s",
                data=[int(ctx.guild.id)]
            )

            if not channel_id:
                return await ctx.send("Welcome system is already disabled", ephemeral=True)

            self.database.execute(
                query="DELETE FROM welcome WHERE channelId=%s AND serverId=%s",
                data=[int(channel_id[0][0]), int(ctx.guild.id)]
            )

            return await ctx.send("The welcome system is now disabled.", ephemeral=True)

        channel_id = self.database.execute(
                query="SELECT channelId FROM welcome WHERE serverId=%s",
                data=[int(ctx.guild.id)]
            )

        if channel_id:
            self.database.execute(
                query="DELETE FROM welcome WHERE channelId=%s AND serverId=%s",
                data=[int(channel_id[0][0]), int(ctx.guild.id)]
            )

            self.database.execute(
                query="INSERT INTO welcome (serverId, channelId) VALUE (%s,%s)",
                data=[int(ctx.guild.id), int(channel.id)]
            )

            return await ctx.send("System now updated.", ephemeral=True)

        self.database.execute(
            query="INSERT INTO welcome (serverId, channelId) VALUE (%s,%s)",
            data=[int(ctx.guild.id), int(channel.id)]
        )

        await ctx.send("Welcome system is now ready to use.", ephemeral=True)


def setup(bot):
    bot.add_cog(WelcomeSetup(bot))
