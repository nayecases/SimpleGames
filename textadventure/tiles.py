import items, enemies

class MapTile():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return "Space:  X {} Y{}".format(self.x, self.y)
    def intro_text(self):
        return NotImplementedError()
    def modify_player(self):
        return NotImplementedError()

class PilotCabin(MapTile):
    def __init__(self):
        MapTile.__init__(self, x = 0, y = 0)
    def intro_text(self):
        return """ It's the pilot cabin.. noone here, I should now better"""
    def modify_player(self):
        #No action on the player
        pass
class JaynesChamber(MapTile)
    def __init__(self):
        self.item = Gun()
        MapTile.__init__(self, x = 1, y = 1)
    def intro_text(self):
        return """ Maybe Jane has something useful here. FAY-FAY duh PEE-yen... it smells!"""
    def modify_player(self):
        #No action on the player
        pass
    def add_item(self, player):
        player.inventory.add(self.item)
