from player import Player
import world

def run():
    world.load_map()
    player = Player("Odin")
    while not player.end:
        

run()
