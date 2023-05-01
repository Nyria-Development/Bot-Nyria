import nextcord
from typing import Optional


class SingleButton(nextcord.ui.View):
    def __init__(self, name: str, button_color: nextcord.ButtonStyle, time: Optional[float] = None):
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
