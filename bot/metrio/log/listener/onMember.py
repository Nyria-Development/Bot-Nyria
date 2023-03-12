import nextcord
from nextcord.ext import commands
from src.dictionaries import logs


class JoinLeft(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        if logs.get_log_on_state(member.guild.id, 1) == 1 and logs.get_log_on_state(member.guild.id,
                                                                                    4) == 1:  # 1 is log, 4 is on_joiner
            log_channel = self.bot.get_channel(logs.get_log_channel(member.guild.id))
            log_embed = nextcord.Embed(title="New User",
                                       description=f"The User {member.mention} just joined this Discord.",
                                       color=0x138200)
            log_embed.set_thumbnail(member.avatar)
            log_embed.set_footer(text=member.joined_at)
            await log_channel.send(embed=log_embed)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        if logs.get_log_on_state(member.guild.id, 1) == 1 and logs.get_log_on_state(member.guild.id,
                                                                                    4) == 1:  # 1 is log, 4 is on_joiner
            log_channel = self.bot.get_channel(logs.get_log_channel(member.guild.id))
            log_embed = nextcord.Embed(title="User Left",
                                       description=f"The User {member.mention} just left this Discord.",
                                       color=0xd50000)
            log_embed.set_thumbnail(member.avatar)
            await log_channel.send(embed=log_embed)

    @commands.Cog.listener()
    async def on_member_update(self, before: nextcord.Member, after: nextcord.Member):
        if logs.get_log_on_state(after.guild.id, 1) == 1 and logs.get_log_on_state(after.guild.id,
                                                                                   4) == 1:  # 1 is log, 4 is on_joiner
            log_channel = self.bot.get_channel(logs.get_log_channel(after.guild.id))
            if before.nick != after.nick:
                log_embed = nextcord.Embed(title="Nickname Update",
                                           description=f"The User {after.mention} updated there Nick.",
                                           color=after.accent_color)
                log_embed.set_thumbnail(after.display_avatar)
                log_embed.add_field(name="befor", value=before.nick)
                log_embed.add_field(name="after", value=after.nick)
                await log_channel.send(embed=log_embed)
            compare_roles = [role for role in before.roles + after.roles if
                             role not in before.roles or role not in after.roles]
            if compare_roles:
                log_embed = nextcord.Embed(title="Role Update",
                                           description=f"{after.mention} Roles were updated.",
                                           color=after.accent_color)
                log_embed.set_thumbnail(after.display_avatar)
                log_embed.add_field(name=("✅ add" if len(before.roles) < len(after.roles) else "❌ removed"),
                                    value=compare_roles[0].mention)
                await log_channel.send(embed=log_embed)


def setup(bot):
    bot.add_cog(JoinLeft(bot))
