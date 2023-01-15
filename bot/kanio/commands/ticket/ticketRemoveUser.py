import nextcord
import nextcord.ext
from nextcord.ext import commands


class TicketRemoveUser(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(
        name="kanio-ticket-remove-user",
        description="Remove an user from a ticket",
        force_global=True,
        default_member_permissions=8
    )
    async def ticket_remove_user(self, ctx: nextcord.Interaction, user: nextcord.Member, ticket: nextcord.TextChannel):
        category = nextcord.utils.get(ctx.guild.categories, name="ticket")

        if len(category.channels) == 0:
            return await ctx.send("There are no tickets.", ephemeral=True)

        if user == ctx.user:
            return await ctx.send("You can't remove yourself.", ephemeral=True)

        for channels in category.channels:
            if str(channels).lower() != str(ticket.name).lower():
                return await ctx.send("This Channel is not in the category **TICKET**", ephemeral=True)

        await ticket.set_permissions(user, view_channel=False)
        await ctx.send(f"The user **{user}** was removed from the ticket.", ephemeral=True)


def setup(bot):
    bot.add_cog(TicketRemoveUser(bot))
