from items import Gun, Credits
from random import randint


class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return "Space:  X {} Y{}".format(self.x, self.y)
    def intro_text(self):
        return NotImplementedError()
    def extended_text():
        return NotImplementedError()
    def modify_player(self):
        return NotImplementedError()

class PilotCabin(MapTile):
    def __init__(self, x, y):
        MapTile.__init__(self, x , y)
        self.bigRedButton = False
        self.item = Toy()
    def intro_text(self):
        return """ It's the pilot cabin.. noone here, I should now better"""
    def extended_text(self):
        return """I look into the black abiss that peeks at me through the wide windows * Sigh *... Oh, look! Wash's dinosaurs!!.
There is some buttons that are lit up, an old blanquet and the special button that Wash prepared"""
    def modify_player(self):
        #No action on the player
        pass

class JaynesChamber(MapTile):
    def __init__(self, x, y):
        self.item = Gun()
        MapTile.__init__(self, x , y)
    def intro_text(self):
        return """ It's Jane's room. FAY-FAY duh PEE-yen... it smells!"""
    def extended_text(self):
        return """Just a regular chamber, a small bed, an old hat, a rack full of weapons... the usual."""
    def modify_player(self):
        #No action on the player
        pass


class EngineRoom(MapTile):
    def __init__(self,x, y,  item):
        self.item = Screwdriver()
        self.usedCatalyzer = False
        MapTile.__init__(self, x , y)
    def intro_text(self):
        return """ This is Kaylee's realm, beware thou who should pass..."""
    def extended_text(self):
        return """The now useless motor lies cold, everything is half lit. There are some tools on the floor."""
    def modify_player(self):
        #No action on the player
        pass


class EmptyCorridor(MapTile):
    extended = ["My steps echoes down the corridor... It reminds me, everybody dies alone","THE HERO OF CANTON, THE MAN THE CALL JAAAAYNE *sings while walking down the corridor*","I wonder... What is like the 'special' hell? *Scratches chin while walking down the corridor*"]
    def __init__(self, x, y):
        MapTile.__init__(self, x, y)
    def intro_text(self):
        return """ Just an empty corridor, it feels so lonely."""
    def extended_text(self):
        return self.extended[randint(0, len(self.extended)-1)]
    def modify_player(self):
        #No action on the player
        pass

class MalsChamber(MapTile):#TODO
    def __init__(self,x, y,  item):
        self.item = Screwdriver()
        MapTile.__init__(self, x , y)
    def intro_text(self):
        return """ This is Kaylee's realm, beware thou who should pass..."""
    def extended_text(self):
        return """The now useless motor lies cold, everything is half lit. There are some tools on the floor."""
    def modify_player(self):
        #No action on the player
        pass


class ZoesNWashsChamber(MapTile):#TODO
    def __init__(self,x, y,  item):
        self.item = Screwdriver()
        MapTile.__init__(self, x , y)
    def intro_text(self):
        return """ This is Kaylee's realm, beware thou who should pass..."""
    def extended_text(self):
        return """The now useless motor lies cold, everything is half lit. There are some tools on the floor."""
    def modify_player(self):
        #No action on the player
        pass


class KayleesChamber(MapTile):#TODO
    def __init__(self,x, y,  item):
        self.item = Screwdriver()
        MapTile.__init__(self, x , y)
    def intro_text(self):
        return """ This is Kaylee's realm, beware thou who should pass..."""
    def extended_text(self):
        return """The now useless motor lies cold, everything is half lit. There are some tools on the floor."""
    def modify_player(self):
        #No action on the player
        pass


class dinningRoom(MapTile):#TODO
    def __init__(self,x, y,  item):
        self.item = Cake()
        MapTile.__init__(self, x , y)
    def intro_text(self):
        return """ This is Kaylee's realm, beware thou who should pass..."""
    def extended_text(self):
        return """The now useless motor lies cold, everything is half lit. There are some tools on the floor."""
    def modify_player(self):
        #No action on the player
        pass


class infirmary(MapTile):#TODO
    def __init__(self,x, y,  item):
        self.item = Adrenaline()
        MapTile.__init__(self, x , y)
    def intro_text(self):
        return """ The irfirmary, there still are some of the stuff used on Zoe..."""
    def extended_text(self):
        return """The Doc patched us oh so many times in here, maybe there is something useful left in the cabinets. An adrenaline shot is left.
I should keep it... for a rainy day"""
    def modify_player(self):
        #No action on the player
        pass


class cargoBay(MapTile):
    def __init__(self,x, y,  item):
        #self.item = Screwdriver()
        MapTile.__init__(self, x , y)
    def intro_text(self):
        return """ Cargo Bay, there is not much left, no jobs for now. Now it's just a big empty space, like a whale belly."""
    def extended_text(self):
        return """There are some boxes left, nothing special, the jeep is under its blanquet... a couple of weigths that Jayne uses..."""
    def modify_player(self):
        #No action on the player
        pass
