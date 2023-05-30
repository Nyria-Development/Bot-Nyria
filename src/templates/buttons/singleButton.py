# All Rights Reserved
# Copyright (c) 2023 Nyria
#
# This code, including all accompanying software, documentation, and related materials, is the exclusive property
# of Nyria. All rights are reserved.
#
# Any use, reproduction, distribution, or modification of the code without the express written
# permission of Nyria is strictly prohibited.
#
# No warranty is provided for the code, and Nyria shall not be liable for any claims, damages,
# or other liability arising from the use or inability to use the code.

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
