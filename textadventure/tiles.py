import items, enemies

class MapTile():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return "Space:  X: {} Y: {}".format(self.x, self.y)
    def intro_text(self):
        return NotImplementedError()
    def extended_text(self):
        return NotImplementedError()
    def modify_player(self):
        return NotImplementedError()

class PilotCabin(MapTile):
    def __init__(self):
        MapTile.__init__(self, x, y)
        self.item = Toy("Dinosaurs")
    def intro_text(self):
        return """ It's the pilot cabin.. noone here, I should now better"""
    def extended_text(self):
        return """I look into the black abiss that peeks at me through the wide windows * Sigh *... Oh, look! Wash's dinosaurs!!"""
    def modify_player(self):
        #No action on the player
        pass
class JaynesChamber(MapTile)
    def __init__(self):
        #self.item = Gun()
        MapTile.__init__(self, x, y )
    def intro_text(self):
        return """ Maybe Jane has something useful here. FAY-FAY duh PEE-yen... it smells!"""
    def modify_player(self):
        #No action on the player
        pass
    def add_item(self, player):
        player.inventory.add(self.item)

class MalChamber(MapTile)
    def __init__(self):
        self.item = Gun()
        MapTile.__init__(self, x , y )
    def intro_text(self):
        return """ Maybe Jane has something useful here. FAY-FAY duh PEE-yen... it smells!"""
    def modify_player(self):
        #No action on the player
        pass
    def add_item(self, player):
        player.inventory.add(self.item)
