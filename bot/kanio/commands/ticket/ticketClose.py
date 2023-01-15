import nextcord
import nextcord.ext
from nextcord.ext import commands, application_checks
from templates import selects, embeds


class TicketClose(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(
        name="kanio-ticket-close",
        description="Close a ticket",
        force_global=True
    )
    @application_checks.has_permissions(administrator=True)
    async def ticket_close(self, ctx: nextcord.Interaction):
        channels = []
        category = nextcord.utils.get(ctx.guild.categories, name="ticket")

        if category is None or len(category.channels) == 0:
            return await ctx.send("Tickets was never created.", ephemeral=True)

        for channel in category.channels:
            channels.append(str(channel.name).lower())

        channel_embed = embeds.TemplateEmbed(
            bot=self.bot,
            ctx=ctx,
            color=nextcord.Color.blurple(),
            description="Ticket | Kanio"
        )
        channel_embed.add_field(
            name="Delete ticket?",
            value=f"If you select a ticket {self.bot.user.name} will delete this ticket",
            inline=False
        )
        channel_selektor = selects.TemplateStringSelect(
            label_name=channels,
            time=60,
            placeholder="Please select a ticket"
        )
        await ctx.send(embed=channel_embed, view=channel_selektor, ephemeral=True)
        await channel_selektor.wait()

        try:
            ticket_name = channel_selektor.select.values[0]
        except IndexError:
            return await ctx.send(":x: | No ticket selected.", ephemeral=True)

        ticket = nextcord.utils.get(category.channels, name=ticket_name)
        await ticket.delete()


def setup(bot):
    bot.add_cog(TicketClose(bot))
