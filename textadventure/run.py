from player import Player
import world, re

def run():
    world.load_map()
    player = Player("Odin")
    while not player.end:
        #print "Action:\n"
        userAction = raw_input("Action:  ")
        if re.match("t", userAction):
            print userAction

run()
