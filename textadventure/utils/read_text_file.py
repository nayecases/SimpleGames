from flavors_terminal import Flavors_terminal as fla



def read_firefly(file_path):
    result = []
    with open(file_path) as file:
        lines = file.readlines()
    for line in lines:
        if line[0] is 'i':
            result.append(fla.ITALIC +line[4:] + fla.ENDC)
        elif line[0] is 'y':
            result.append(fla.GREY + line[4:] +fla.ENDC)
        elif line[0] is 'z':
            result.append(fla.GREY + fla.ITALIC + line[4:] +fla.ENDC)
        elif line[0] is 'n':
            result.append(line[4:] +fla.ENDC)
        elif line[0] is 'r':
            result.append(fla.RED + line[4:] +fla.ENDC)
        elif line[0] is 'b':
            result.append( fla.BOLD +line[4:] + fla.ENDC)
        elif line[0] is 'g':
            result.append(fla.GEEN + line[4:] +fla.ENDC)
        elif line[0] is 'g':
            result.append(fla.GEEN + line[4:] +fla.ENDC)
        elif line[0] is 'e':
            result.append(fla.RED + line[4:] +fla.ENDC)
    return result


test =  read_firefly('resources/introduction.txt')
