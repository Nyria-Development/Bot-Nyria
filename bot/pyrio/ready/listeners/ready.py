# All Rights Reserved
# Copyright (c) 2023 Nyria
#
# This code, including all accompanying software, documentation, and related materials, is the exclusive property
# of Nyria. All rights are reserved.
#
# Any use, reproduction, distribution, or modification of the code without the express written
# permission of Nyria is strictly prohibited.
#
# No warranty is provided for the code, and Nyria shall not be liable for any claims, damages,
# or other liability arising from the use or inability to use the code.

from nextcord.ext import commands
from src.logger.logger import Logging


async def ready(bot_user):
    Logging().info(f"Bot is logged in as: {bot_user}")
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
    pass
