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


class StringSelect(nextcord.ui.View):
    def __init__(self, label_name: list, placeholder: str):
        super().__init__()
        self.label_name = label_name
        self.placeholder = placeholder

        self.options = []

        for element in self.label_name:
            self.options.append(
                nextcord.SelectOption(
                    label=str(element)
                )
            )

        async def callback(ctx: nextcord.Interaction):
            self.stop()

        self.select = nextcord.ui.StringSelect(
            options=self.options,
            placeholder=self.placeholder
        )

        self.select.callback = callback
        self.add_item(self.select)
