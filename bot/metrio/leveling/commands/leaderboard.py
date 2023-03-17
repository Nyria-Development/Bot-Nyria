import nextcord
from nextcord.ext import commands
from src.loader.jsonLoader import Leveling


class LevelLeaderboard(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(
        name="metrio-discord-level_leaderboard",
        description="Find the best Users on this Discord",
        force_global=True
    )
    async def level_leaderboard(
            self,
            ctx: nextcord.Interaction
    ) -> None:

        """
        Attributes
        ----------
        :param ctx: Gives the discord interaction
        :return: None
        ----------
        """

        user_list = Leveling().get_levels()
        new_user_list = sorted(user_list, key=lambda d: d['xp'], reverse=True)

        level_embed = nextcord.Embed(
            title="LeaderBoard",
            description=f"Leaderboard of the 10 highest ranked users.",
            color=0x081e8c
        )

        for i, user in enumerate(new_user_list):
            if i < 10:
                level_embed.add_field(name=f"{i+1} - {user['discordUser']}", value=f"Level: {user['level']}, XP: {user['xp']}")
            else:
                break
        await ctx.send(embed=level_embed, ephemeral=False)


def setup(bot):
    bot.add_cog(LevelLeaderboard(bot))
