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

import json


class GetCredits:
    def __init__(self):
        with open("resources/credits/credits.json", "r") as c:
            self.__config = json.load(c)

    def get_credits(self):
        return self.__config
