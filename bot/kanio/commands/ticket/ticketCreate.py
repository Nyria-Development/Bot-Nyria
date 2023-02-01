import nextcord
import nextcord.ext
from nextcord.ext import commands
from src.templates import embeds, buttons


class TicketCreate(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(
        name="kanio-ticket",
        description="Do you need help? Here you can create a ticket.",
        force_global=True
    )
    async def ticket_create(self, ctx: nextcord.Interaction):
        category = nextcord.utils.get(ctx.guild.categories, name="ticket")

        if category is None:
            category = await ctx.guild.create_category(name="ticket")

        if len(category.channels) >= 25:
            return await ctx.send("There are to many tickets. Please try again later.", ephemeral=True)

        for channel in category.channels:
            if channel.name == f"ticket-{str(ctx.user.name).lower()}":
                return await ctx.send("You have an active ticket. Please use that.", ephemeral=True)

        create_ticket_embed = embeds.TemplateEmbed(
            bot=self.bot,
            ctx=ctx,
            color=nextcord.Color.blurple(),
            description="Channel | Kanio"
        )
        create_ticket_embed.add_field(
            name="Terms & Conditions",
            value="By clicking the button, you accept Discord's TOS.",
            inline=False
        )
        create_ticket_button_accept = buttons.TemplateButtonTicket(
            name="Accept",
            button_color=nextcord.ButtonStyle.red,
            time=60 * 10
        )
        await ctx.send(embed=create_ticket_embed, view=create_ticket_button_accept, ephemeral=True)
        await create_ticket_button_accept.wait()

        if not create_ticket_button_accept.pressed:
            return await ctx.send(":x: | You don't have accept the TOS.", ephemeral=True)

        ticket = await ctx.guild.create_text_channel(name=f"ticket-{str(ctx.user.name).lower()}", category=category)
        await ticket.set_permissions(ctx.user, view_channel=True)
        await ticket.set_permissions(ctx.guild.default_role, view_channel=False)

        await ticket.send(f"Hey {ctx.user.mention}, how can we help you?")
        await ctx.send(":white_check_mark: | Ticket was created successful.", ephemeral=True)


def setup(bot):
    bot.add_cog(TicketCreate(bot))
