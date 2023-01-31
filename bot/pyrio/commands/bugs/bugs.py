import nextcord
from nextcord.ext import commands
from src.templates import embeds
from database import connectDatabase


class Bugs(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.connection_pool = connectDatabase.Database().connect(
            pool_name="pool_bugs",
            pool_size=2
        )

    @nextcord.slash_command(
        name="pyrio-bug",
        description="You found a bug? Here you can report it.",
        force_global=True
    )
    async def bugs(self, ctx: nextcord.Interaction, bug: str):
        report_user = ctx.user

        connection = self.connection_pool.get_connection()
        cursor = connection.cursor(prepared=True)

        query = "SELECT reports FROM bug_reports WHERE userId=%s"
        data = [int(report_user.id)]

        cursor.execute(query, data)
        reports = cursor.fetchall()

        if not reports:
            query = "INSERT INTO bug_reports (userId, reports) VALUE (%s,%s)"
            data = (int(report_user.id), 1)

            cursor.execute(query, data)
            connection.commit()
            connection.close()

        if reports and int(reports[0][0]) < 10:
            query = f"UPDATE bug_reports SET reports={int(reports[0][0]) + 1} WHERE userId=%s"
            data = [int(report_user.id)]

            cursor.execute(query, data)
            connection.commit()
            connection.close()

        if reports and int(reports[0][0]) >= 10:
            connection.close()
            return await ctx.send("Please wait before you report a bug again.", ephemeral=True)

        embed_bugs = embeds.TemplateEmbed(
            bot=self.bot,
            ctx=ctx,
            description="Core | Pyrio",
            color=nextcord.Color.brand_green()
        )
        embed_bugs.set_thumbnail(url=ctx.user.avatar)
        embed_bugs.add_field(name="Bug Description", value=bug)

        if len(bug) > 1024:
            return await ctx.send("This report is to long.", ephemeral=True)

        user = await self.bot.fetch_user(817657386751754251)
        await user.send(embed=embed_bugs)
        await ctx.send("Thanks for reporting.", ephemeral=True)


def setup(bot):
    bot.add_cog(Bugs(bot))
