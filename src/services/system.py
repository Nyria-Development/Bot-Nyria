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

import platform
import os
import sys
from src.logger.logger import Logging


class Os:
    @staticmethod
    def locate() -> str:

        """
        Attributes
        ----------
        :return: str
        ----------
        """

        return platform.system()

    @staticmethod
    def check_permissions() -> None:

        """
        Attributes
        ----------
        :return: None
        ----------
        """

        while True:
            if os.geteuid() == 0:
                Logging().warn("You run the bot as root! Continue? (y/n)")
                state = input("> ")

                if state.lower() == "y":
                    break
                elif state.lower() == "n":
                    sys.exit()
                else:
                    continue
            break
