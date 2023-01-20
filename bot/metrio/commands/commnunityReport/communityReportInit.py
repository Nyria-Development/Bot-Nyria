import nextcord
from nextcord.ext import commands
from database import connectDatabase


class CommunityReportInit(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.connection_pool = connectDatabase.Database().connect(
            pool_name="pool_community_report_init",
            pool_size=1
        )

    @nextcord.slash_command(
        name="metrio-community-report-init",
        description="Configure the report system.",
        force_global=True,
        default_member_permissions=8
    )
    async def community_report_init(self, ctx: nextcord.Interaction, reaction: int):
        connection = self.connection_pool.get_connection()
        cursor = connection.cursor(prepared=True)

        query = "SELECT reactions FROM community_report WHERE serverId=%s"
        data = [int(ctx.guild.id)]

        cursor.execute(query, data)
        reaction_counter = cursor.fetchall()

        if not reaction_counter:
            query = "INSERT INTO community_report (serverId, reactions) VALUE (%s,%s)"
            data = (int(ctx.guild.id), reaction)
            cursor.execute(query, data)

            connection.commit()
            connection.close()
            return await ctx.send(f"Community report set to limit **{reaction}**.", ephemeral=True)

        query = f"UPDATE community_report SET reactions={reaction} where serverId=%s"
        data = [int(ctx.guild.id)]

        cursor.execute(query, data)
        connection.commit()
        connection.close()

        await ctx.send(f"Community report set to limit **{reaction}**.", ephemeral=True)


def setup(bot):
    bot.add_cog(CommunityReportInit(bot))
