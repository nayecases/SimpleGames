_world = {}
starting_position = (0, 0)

def load_map():
    with open('resources/serenity.txt', 'r') as map:
        rows = map.readlines()
    x_max = len(rows[0].split('\t'))+1

    for y in range(len(rows)):
        cols = rows[y].split()

        for x in range(x_max):

            tile_name = cols[x].replace('\n', '')
            if tile_name == 'PilotCabin':
                global starting_position
                starting_position = (x, y)
            _world[(x, y)] = None if tile_name == '' else getattr(__import__('rooms'), tile_name)(x, y)

load_map()
#print _world
