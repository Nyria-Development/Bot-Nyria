import nextcord
from nextcord import PartialInteractionMessage, WebhookMessage
from nextcord.ext import commands
from src.templates.embeds.ctxEmbed import CtxEmbed
from src.logger.logger import Logging
from src.database.core.engine import SQLEngine
from src.database.core.session import SQLSession
from sqlalchemy import select, update
from src.database.tables.bugs import TableBugs


class BugsReport(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(
        name="pyrio-bug-report",
        description="You found a bug? Here you can report it.",
        force_global=True
    )
    async def bugs(
            self,
            ctx: nextcord.Interaction,
            bug: str
    ) -> PartialInteractionMessage | WebhookMessage:

        """
        Attributes
        ----------
        :param ctx: Gives the discord interaction
        :param bug: Gives the bug description
        :return: None
        ----------
        """

        Logging().info(f"Command :: pyrio-bug-report :: {ctx.guild.name} :: {ctx.user}")

        if len(bug) > 1024:
            return await ctx.send("This report is to long. Please write it a little bit shorter.", ephemeral=True)

        db_con = SQLEngine.engine.connect()
        db_session = SQLSession.create_session()

        query = select(TableBugs).where(TableBugs.user_id == ctx.user.id)
        reports = db_con.execute(query).all()

        if not reports:
            query = TableBugs(
                user_id=ctx.user.id,
                reports=1
            )
            db_session.add(query)
            db_session.commit()

        if reports and int(reports[0][2]) < 10:
            query = update(TableBugs).values(reports=int(reports[0][2]) + 1).where(TableBugs.user_id == ctx.user.id)
            db_con.execute(query)
            db_con.commit()

        if reports and int(reports[0][2]) >= 10:
            return await ctx.send("Please wait before you report a bug again.", ephemeral=True)

        embed_bugs = CtxEmbed(
            bot=self.bot,
            ctx=ctx,
            color=nextcord.Color.brand_green(),
            description="Core | Pyrio"
        )
        embed_bugs.set_thumbnail(
            url=ctx.user.avatar
        )
        embed_bugs.add_field(
            name="Bug Description",
            value=bug
        )

        db_session.close()
        db_con.close()

        user = await self.bot.fetch_user(817657386751754251)
        await user.send(embed=embed_bugs)
        await ctx.send("Thanks for reporting.", ephemeral=True)


def setup(bot):
    bot.add_cog(BugsReport(bot))
