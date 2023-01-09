import cmd


class Cli(cmd.Cmd):
    def __init__(self):
        super().__init__()
        self.intro = "Nyria"
        self.prompt = "[Nyria]> "

    @staticmethod
    def do_exit(arg):
        exit()
