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

import datetime
from colorama import Fore, Style


class Logging:
    def __init__(self):
        self.now = datetime.datetime.now()
        self.date = self.now.strftime("%d/%m/%Y")
        self.time = self.now.strftime("%H:%M:%S")

    def info(self, msg: str):
        print(f"[{self.date}] [{self.time}] {Fore.GREEN}[info]> {msg} {Style.RESET_ALL}")

    def warn(self, msg: str):
        print(f"[{self.date}] [{self.time}] {Fore.YELLOW}[warn]> {msg} {Style.RESET_ALL}")

    def error(self, msg: str):
        print(f"[{self.date}] [{self.time}] {Fore.RED}[error]> {msg} {Style.RESET_ALL}")
