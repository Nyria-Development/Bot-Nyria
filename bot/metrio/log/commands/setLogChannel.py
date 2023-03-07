import json
import nextcord
from nextcord.ext import commands
from src.loader.jsonLoader import metrio
from src.templates import embeds


class setLogChannel(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.new_guild = {}

    @nextcord.slash_command(
        name="set_log_channel",
        description="sets a LogChannel for this Discord",
        force_global=True,
        default_member_permissions=8
    )
    async def set_log_channel(self, ctx: nextcord.Interaction, log_channel: nextcord.TextChannel):
        print(log_channel)
        guild_list = metrio().get_guilds()
        if any(guild['guild_id'] == ctx.guild_id for guild in guild_list):
            for guild in guild_list:
                if guild['guild_id'] == ctx.guild_id:
                    guild['log_channel_id'] = log_channel.id
                    with open('resources/config/guilds.json', 'w') as file:
                        json.dump(guild_list, file, indent=4)
                    await ctx.send("Updated")
                    break
        else:
            new_guild = {"guild_id": ctx.guild_id, "log_channel_id": log_channel.id, "show_log_for": {"message": True, "join_and_left": True}}
            guild_list.append(new_guild)
            with open('resources/config/guilds.json', 'w') as file:
                json.dump(guild_list, file, indent=4)
            await ctx.send("NewGuild + Updated")


    @nextcord.slash_command(
        name="show_log_channel",
        description="shows the LogChannel for this Discord",
        force_global=True,
        default_member_permissions=8
    )
    async def show_log_channel(self, ctx: nextcord.Interaction):
        print(ctx)



def setup(bot):
    bot.add_cog(setLogChannel(bot))
