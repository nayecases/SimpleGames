import flavors_terminal as fla
from random import randint


def read_firefly(file_path):
    result = []
    with open(file_path) as file:
        lines = file.readlines()
    for line in lines:
        result.append(read_line(line))
    return result

def read_line(line):
    if line[0] is 'i':
        result = fla.con_it(line[4:])
    elif line[0] is 'y':
        result = fla.con_gray(line[4:])
    elif line[0] is 'z':
        result = fla.con_gray_it(line[4:])
    elif line[0] is 'n':
        result = fla.con_def(line[4:])
    elif line[0] is 'r':
        result = fla.con_red(line[4:])
    elif line[0] is 'b':
        result = fla.con_bold(line[4:])
    elif line[0] is 'g':
        result = fla.con_green(line[4:])
    elif line[0] is 'p':
        result = fla.con_purple(line[4:])

    return result

def read_random_line(file_path):
    with open(file_path) as file:
        lines =  file.readlines()
        return read_line(lines[randint(0, len(lines)-1)])

print read_random_line('resources/insults.txt')
