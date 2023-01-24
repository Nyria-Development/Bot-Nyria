import nextcord
from nextcord.ext import commands
import datetime
from database import connectDatabase


class CommunityReport(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.connection_pool = connectDatabase.Database().connect(
            pool_name="pool_community_report",
            pool_size=3
        )

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction: nextcord.Reaction, user: nextcord.Member):
        if reaction.emoji.name != ":warning:":
            return

        connection = self.connection_pool.get_connection()
        cursor = connection.cursor(prepared=True)

        query = "SELECT reactions FROM community_report WHERE serverId=%s"
        data = [int(reaction.message.guild.id)]

        cursor.execute(query, data)
        reactions = cursor.fetchall()

        if not reactions:
            return

        if int(reactions[0][0]) == reaction.count:
            await user.timeout(timeout=datetime.timedelta(hours=4))
            await reaction.message.author.send(f"You are timed out for 4 hours on {reaction.message.guild}.")
            await reaction.message.delete()


def setup(bot):
    bot.add_cog(CommunityReport(bot))
