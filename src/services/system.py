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
