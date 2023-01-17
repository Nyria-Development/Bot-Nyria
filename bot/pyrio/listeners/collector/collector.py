import nextcord
from nextcord.ext import commands
from database import connectDatabase


class Collector(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.connection_pool = connectDatabase.Database().connect(
            pool_name="pool_collector",
            pool_size=2
        )

    @commands.Cog.listener()
    async def on_guild_join(self, ctx: nextcord.Interaction):
        connection = self.connection_pool.get_connection()
        cursor = connection.cursor(prepared=True)

    @commands.Cog.listener()
    async def on_guild_remove(self, ctx: nextcord.Interaction):
        pass


def setup(bot):
    bot.add_cog(Collector(bot))
