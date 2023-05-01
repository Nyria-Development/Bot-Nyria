from nextcord.ext import commands
from src.logger.logger import Logging


class Ready(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        Logging().info(f"Bot is logged in as: {self.bot.user}")
        print("""
            )                      
         ( /(                      
         )\()) (     (   (      )  
        ((_)\  )\ )  )(  )\  ( /(  
         _((_)(()/( (()\((_) )(_)) 
        | \| | )(_)) ((_)(_)((_)_  
        | .` || || || '_|| |/ _` | 
        |_|\_| \_, ||_|  |_|\__,_| 
               |__/  
        """)


def setup(bot):
    bot.add_cog(Ready(bot))
