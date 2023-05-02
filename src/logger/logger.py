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
