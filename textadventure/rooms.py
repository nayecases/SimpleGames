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
    def __init__(self, x, y):
        MapTile.__init__(self, x , y)
    def intro_text(self):
        return """ It's the pilot cabin.. noone here, I should now better"""
    def modify_player(self):
        #No action on the player
        pass

class JaynesChamber(MapTile):
    def __init__(self, x, y):
        self.item = Gun()
        MapTile.__init__(self, x, y )
    def intro_text(self):
        return """ Maybe Jane has something useful here. FAY-FAY duh PEE-yen... it smells!"""
    def modify_player(self):
        #No action on the player
        pass
    def add_item(self, player, item):
        player.inventory.add(item)

class EngineRoom(MapTile):
    def __init__(self,x, y,  item):
        self.item = Screwdriver()
        MapTile.__init__(self, x, y)
    def intro_text(self):
        return """ This is Kaylee's realm, beware thou who should pass... What's that? It's a screwdriver"""
    def modify_player(self):
        #No action on the player
        pass
    def ad_item(self, player, item):
        player.inventory.add(item)

class EmptyCorridor(MapTile):
    def __init__(self, x, y):
        MapTile.__init__(self, x, y)
    def intro_text(self):
        return """ Just an empty corridor, it feels so lonely."""
    def modify_player(self):
        #No action on the player
        pass
