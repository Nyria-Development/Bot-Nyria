import asyncio
import nextcord
from typing import Any, Coroutine
from src.templates.buttons.singleButton import SingleButton
from nextcord import Message, PartialInteractionMessage, WebhookMessage
from nextcord.ext import commands
from src.logger.logger import Logging
from src.loader.voting import GetVoting
from src.templates.embeds.ctxEmbed import CtxEmbed


class CreateVoting(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(
        name="kanio-create-voting",
        description="Create a voting",
        force_global=True,
        default_member_permissions=8
    )
    async def create_voting(
            self,
            ctx: nextcord.Interaction,
            question: str = nextcord.SlashOption(
                description="Write your question.",
                required=True
            ),
            answers: str = nextcord.SlashOption(
                description="How many answers would you like?",
                choices=GetVoting().get_voting()[0]
            ),
            role: nextcord.Role = nextcord.SlashOption(
                description="The role you want to ping.",
                required=False
            )
    ) -> Message | Coroutine[Any, Any, PartialInteractionMessage | WebhookMessage]:

        """
        Attributes
        ----------
        :param ctx:
        :param question:
        :param answers:
        :param role:
        :return: Message
        ----------
        """

        Logging().info(f"Command :: kanio-create-voting :: {ctx.guild.name} :: {ctx.user}")

        await ctx.response.defer()

        embed_voting = CtxEmbed(
            bot=self.bot,
            ctx=ctx,
            color=nextcord.Color.blurple(),
            description="Kanio | Channel"
        )
        embed_voting.add_field(
            name="Question",
            value=question,
            inline=False
        )

        emote_list = list()

        for answer in range(0, int(answers)):
            while True:
                await ctx.user.send(f"Please write your {answer + 1}. answer: ")

                try:
                    msg: nextcord.Message = await self.bot.wait_for("message", timeout=60 * 4)
                except asyncio.TimeoutError:
                    await ctx.send("Voting Canceled", ephemeral=True)
                    return await ctx.user.send("Voting Canceled")

                if msg.author.bot:
                    await msg.delete()
                    continue
                break

            while True:
                await ctx.user.send("React to **this** message you want the emote.")

                try:
                    reaction: tuple = await self.bot.wait_for("reaction_add", timeout=60 * 4)
                except asyncio.TimeoutError:
                    await ctx.send("Voting Canceled", ephemeral=True)
                    return await ctx.user.send("Voting Canceled")

                if str(reaction[0]).startswith("<"):
                    await ctx.user.send("Please don't use custom emotes.")
                    continue
                break

            embed_voting.add_field(
                name=f"{answer + 1}. Answer {reaction[0]}",
                value=msg.content,
                inline=False
            )
            emote_list.append(reaction[0])

        button_voting = SingleButton(
            name="Start voting",
            button_color=nextcord.ButtonStyle.green,
            time=60.0
        )
        await ctx.user.send(embed=embed_voting, view=button_voting)
        await button_voting.wait()

        if not button_voting.pressed:
            return await ctx.send("Voting canceled.", ephemeral=True)

        if role is not None:
            voting = await ctx.send(content=f"{role.mention} new voting started!", embed=embed_voting)
        else:
            voting = await ctx.send(content=f"New voting started!", embed=embed_voting)

        for react in emote_list:
            await voting.add_reaction(emoji=react)


def setup(bot):
    bot.add_cog(CreateVoting(bot))
