from flavors_terminal import Flavors_terminal as fla



def read_firefly(file_path):
    with open(file_path) as file:
        lines = file.readlines()
    for line in lines:
        if line[0] is 'i':
            print  + line[4:] +
        elif line[0] is 'r':
            print Colors_terminal.ITEM + line[4:] +Colors_terminal.NORMAL


read_firefly('resources/ending.txt')
