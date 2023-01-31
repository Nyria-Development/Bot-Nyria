import nextcord.ext


class TemplateButtonNormal(nextcord.ui.View):
    def __init__(self, name: str, button_color: nextcord.ButtonStyle, time: int):
        super().__init__()
        self.name = name
        self.button_color = button_color
        self.timeout = time
        self.pressed = False

        async def callback(ctx: nextcord.Interaction):
            self.pressed = True
            self.stop()

        self.button = nextcord.ui.Button(label=self.name, style=self.button_color)
        self.button.callback = callback
        self.add_item(self.button)


class TemplateButtonUrl(nextcord.ui.View):
    def __init__(self, name: str, url: str, time: int):
        super().__init__()
        self.name = name
        self.url = url
        self.timeout = time

        self.url_button = nextcord.ui.Button(label=self.name, style=nextcord.ButtonStyle.url, url=self.url)
        self.add_item(self.url_button)


class TemplateButtonTicket(nextcord.ui.View):
    def __init__(self, name: str, button_color: nextcord.ButtonStyle, time: int):
        super().__init__()
        self.name = name
        self.button_color = button_color
        self.timeout = time
        self.pressed = False

        async def callback(ctx: nextcord.Interaction):
            self.pressed = True
            self.stop()

        self.button = nextcord.ui.Button(label=self.name, style=self.button_color)
        self.button.callback = callback

        self.button_dc_tos = nextcord.ui.Button(
            label="Discord TOS",
            style=nextcord.ButtonStyle.url,
            url="https://discord.com/terms"
        )

        self.add_item(self.button)
        self.add_item(self.button_dc_tos)
