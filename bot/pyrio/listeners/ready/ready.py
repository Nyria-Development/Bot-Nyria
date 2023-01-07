from nextcord.ext import commands
import threading
from website import site


class Ready(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Bot is logged in as: {self.bot.user}")
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

        # start flask server
        threading.Thread(target=site.WebserverNyria).start()


def setup(bot):
    bot.add_cog(Ready(bot))
