import nextcord
from nextcord.ext import commands
from bot.metrio.leveling.listener import experience
from src.dictionaries import logs


class Reaction(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        if logs.get_log_on_state(payload.guild_id, 1) == 1 and logs.get_log_on_state(payload.guild_id, 3) == 1: # 1 is log, 2 is reaction
            log_channel = self.bot.get_channel(logs.get_log_channel(payload.guild_id))
            reaction_channel = await self.bot.fetch_channel(payload.channel_id)
            reaction_message = await reaction_channel.fetch_message(payload.message_id)
            log_embed = nextcord.Embed(title="New Reaction",
                                       description=f"A new Reaction was added in {reaction_channel.mention} by {payload.member.mention}.",
                                       color=0x081e8c)
            log_embed.add_field(name="Reaction:", value=payload.emoji)
            log_embed.add_field(name="Message:", value=reaction_message.jump_url)
            await log_channel.send(embed=log_embed)


    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        if logs.get_log_on_state(payload.guild_id, 1) == 1 and logs.get_log_on_state(payload.guild_id, 3) == 1:
            log_channel = self.bot.get_channel(logs.get_log_channel(payload.guild_id))
            reaction_channel = await self.bot.fetch_channel(payload.channel_id)
            reaction_message = await reaction_channel.fetch_message(payload.message_id)
            log_embed = nextcord.Embed(title="Reaction Removed",
                                       description=f"A Reaction was removed in {reaction_channel.mention}.",
                                       color=0x081e8c)
            log_embed.add_field(name="Reaction:", value=payload.emoji)
            log_embed.add_field(name="Message:", value=reaction_message.jump_url)
            await log_channel.send(embed=log_embed)



def setup(bot):
    bot.add_cog(Reaction(bot))
