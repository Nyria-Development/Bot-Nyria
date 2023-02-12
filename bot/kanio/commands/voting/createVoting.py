import nextcord
from nextcord.ext import commands
from src.templates import embeds
import asyncio
from src.loader import jsonLoader
from src.templates import buttons


class CreateVoting(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(
        name="kanio-voting-create",
        description="Create a voting",
        force_global=True
    )
    async def create_voting(self,
                            ctx: nextcord.Interaction,
                            question: str,
                            answer: str = nextcord.SlashOption(name="vote", choices=asyncio.run(jsonLoader.JsonLoader().get_voting_numbers()))):
        await ctx.response.defer()

        user_answers = []
        nums: dict = {
            1: "1️⃣",
            2: "2️⃣",
            3: "3️⃣",
            4: "4️⃣",
            5: "5️⃣",
            6: "6️⃣"
        }

        embed_voting = embeds.TemplateEmbed(
            bot=self.bot,
            ctx=ctx,
            description="Kanio | Channel",
            color=nextcord.Color.blurple()
        )
        embed_voting.add_field(name="Question", value=question, inline=False)

        for i in range(0, int(answer)):
            await ctx.user.send(f"Please write your {i + 1}. answer: ")

            try:
                msg: nextcord.Message = await self.bot.wait_for("message", timeout=60*4)
            except asyncio.TimeoutError:
                return await ctx.send("Canceled Voting", ephemeral=True)

            user_answers.append(msg.content)

        count = 1
        for element in user_answers:
            embed_voting.add_field(name=f"{nums[count]}", value=element, inline=False)
            count += 1

        button_voting = buttons.TemplateButtonNormal(
            name="Start Voting",
            button_color=nextcord.ButtonStyle.green,
            time=60
        )
        await ctx.user.send(embed=embed_voting, view=button_voting)
        await button_voting.wait()

        if not button_voting.pressed:
            return ctx.send("Voting canceled.", ephemeral=True)

        voting = await ctx.send(embed=embed_voting)

        for i in range(1, len(user_answers) + 1):
            await voting.add_reaction(emoji=nums[i])


def setup(bot):
    bot.add_cog(CreateVoting(bot))
