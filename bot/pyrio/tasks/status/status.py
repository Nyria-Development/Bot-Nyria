import nextcord
from nextcord.ext import commands, tasks
import asyncio


class Status(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # Show the status in discord
    @tasks.loop(seconds=30)
    async def status(self):
        await self.bot.change_presence(
            activity=nextcord.Game("Imagination is way more important than knowledge."),
            status=nextcord.Status.do_not_disturb
        )
        await asyncio.sleep(15)
        await self.bot.change_presence(
            activity=nextcord.Game(f"Nyria supported {len(self.bot.guilds)} Server."),
            status=nextcord.Status.do_not_disturb
        )

    # start the status
    @commands.Cog.listener()
    async def on_ready(self):
        await self.status.start()
        print("Status started")


def setup(bot):
    bot.add_cog(Status(bot))
