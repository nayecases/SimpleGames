from player import Player
import world, re


commands = {r'\bALIVE\b': 'isAlive', r'\bINVENTORY\b': 'printInventory', r'\bN\b':'moveNorth', r'\bNORTH\b':'moveNorth', r'\bS\b':'moveSouth', r'\bSOUTH\b':'moveSouth', r'\bE\b':'moveEast', r'\bEAST\b':'moveEast', r'\bW\b':'moveWest', r'\bWEST\b':'moveWest',
 r'\bATTACK\b' : 'attack', r'\bINSULT\b':'insult', r'\bWHERE\b':'whereAmI' }
def run():
    world.load_map()
    player = Player("Odin")
    while not player.end:
        #print "Action:\n"
        userActionRaw = raw_input(":  ")
        userAction = userActionRaw.split(" ")
        params= []
        if len(userAction)>1:
            params = userAction[1:]
        #if re.match("t", userAction):
        for key in commands:
            if re.match(key, userAction[0].upper()):
                #print "pasa"
                res = getattr(player, commands[key])(*params)
                #print res


run()
