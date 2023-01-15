import nextcord.ext


class TemplateStringSelect(nextcord.ui.View):
    def __init__(self, label_name: list, placeholder: str, time: int):
        super().__init__()
        self.label_name = label_name
        self.options = []
        self.timeout = time
        self.placeholder = placeholder

        for element in self.label_name:
            self.options.append(nextcord.SelectOption(label=str(element)))

        async def callback(ctx: nextcord.Interaction):
            self.stop()

        self.select = nextcord.ui.StringSelect(
            options=self.options,
            placeholder=self.placeholder,
        )
        self.select.callback = callback
        self.add_item(self.select)
