_world = {}
starting_position = (0, 0)

def load_map():
    with open('resources/serenity.txt', 'r') as map:
        rows = map.readlines()

    #x_max = len(rows[2].split())
    #print range(x_max)
    for y in range(len(rows)):
        cols = rows[y].split()

        for x in range(len(cols)):

            tile_name = cols[x].replace('\n', '')
            if tile_name == 'PilotCabin':
                global starting_position
                starting_position = (x, y)
            _world[(x, y)] = None if tile_name == '' else getattr(__import__('rooms'), tile_name)(x, y)

load_map()



def room_exists(cx, cy):
    return _world.get((cx, cy))

#print room_exists(3,1)
#print _world
