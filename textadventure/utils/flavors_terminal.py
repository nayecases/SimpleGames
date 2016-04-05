

class Flavors_terminal:
    GREEN = '\033[92m'
    GREY = '\033[37m'
    RED = '\033[91m'
    ITALIC = '\033[3m'
    BOLD = '\033[1m'
    ENDC = '\033[0m'
    ERROR = '\033[33m'
    PURPLE = '\033[94m'


def con_green(line):
    return Flavors_terminal.GREEN + line +Flavors_terminal.ENDC
def con_it(line):
    return Flavors_terminal.ITALIC +line + Flavors_terminal.ENDC
def con_gray(line):
    return Flavors_terminal.GREY + line +Flavors_terminal.ENDC
def con_def(line):
    return line +Flavors_terminal.ENDC
def con_red(line):
    return Flavors_terminal.RED + line +Flavors_terminal.ENDC
def con_bold(line):
    return Flavors_terminal.BOLD +line + Flavors_terminal.ENDC
def con_purple(line):
    return Flavors_terminal.PURPLE + line +Flavors_terminal.ENDC
def con_gray_it(line):
    return Flavors_terminal.GREY + Flavors_terminal.ITALIC + line +Flavors_terminal.ENDC
def con_error(line):
    return Flavors_terminal.ERROR + line + Flavors_terminal.ENDC
