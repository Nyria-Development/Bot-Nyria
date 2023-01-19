import nextcord
from nextcord.ext import commands
from database import connectDatabase


class BlacklistAddWord(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.connection_pool = connectDatabase.Database().connect(
            pool_name="pool_add_words",
            pool_size=3
        )

    @nextcord.slash_command(
        name="metrio-blacklist-add-word",
        description="Add words to the blacklist.",
        force_global=True,
        default_member_permissions=8
    )
    async def add_word(self, ctx: nextcord.Interaction, word: str):
        connection = self.connection_pool.get_connection()
        cursor = connection.cursor(prepared=True)

        query = "SELECT word FROM blacklist WHERE serverId=%s"
        data = [int(ctx.guild.id)]

        cursor.execute(query, data)
        words = cursor.fetchall()

        if words:
            if len(words[0]) >= 50:
                return await ctx.send("You can add a maximum of 50 words.", ephemeral=True)

            for w in words[0]:
                if str(w).lower() == word.lower():
                    return await ctx.send("This word exists.", ephemeral=True)

        query = "INSERT INTO blacklist (serverId, word) VALUE (%s,%s)"
        data = (int(ctx.guild.id), str(word).lower())

        cursor.execute(query, data)
        connection.commit()
        connection.close()

        await ctx.send("Word was added successful.", ephemeral=True)


def setup(bot):
    bot.add_cog(BlacklistAddWord(bot))
