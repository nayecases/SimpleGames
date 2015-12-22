from player import Player
import world, re


commands = {'IS ALIVE': 'isAlive', 'INVENTORY': 'printInventory', 'N':'moveNorth', 'NORTH':'moveNorth', 'S':'moveSouth', 'SOUTH':'moveSouth', 'E':'moveEast', 'EAST':'moveEast', 'W':'moveWest', 'WEST':'moveWest', 'ATTACK' : 'attack' }
def run():
    world.load_map()
    player = Player("Odin")
    while not player.end:
        #print "Action:\n"
        userAction = raw_input(":  ")
        #if re.match("t", userAction):
        for key in commands:
            if re.match(key, userAction.upper()):
                res = getattr(player, commands[key])()
                #print res

run()
