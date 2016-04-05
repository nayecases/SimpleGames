from items import Gun, Credits
from random import randint
import utils.flavors_terminal as fla
import utils.read_text_file as read
import world


class Player:
    def __init__(self, name):
        self.runTime = { "timer":0, "exchange": False, "usedCatalyzer": False, "bigDamnRedButton": False, "error" : "I don\'t understand that", "roundsTilCapt" : 10, "secDialog": 1, "end": False, "insults":"resources/insults.txt"}
        self.name = name
        self.health = 100
        self.inventory = [Credits(30, specialRoom = None), Gun(specialRoom = None)]
        self.locationX, self.locationY = world.starting_position

    def __str__(self):
        return "\nName: {}, health: {}\n".format(self.name, self.health)
    def isAlive(self):
        if self.health > 0:
            print fla.con_gray("All good so far")
        else:
            print fla.con_gray("... tell my mother I love her")
    def hasItemInInventory(self, itemName):
        for item in self.inventory:
            if item.name == itemName:
                return item
    def printInventory(self):
        for item in self.inventory:
            print item
    def move(self, dx, dy):
        self.locationX +=dx
        self.locationY +=dy
        if world.room_exists(self.locationX, self.locationY):
            self.whereAmI()
        else:
            self.locationX -=dx
            self.locationY -=dy
            print fla.con_gray("""I can't go there!""")
    def moveNorth(self):
        self.move(dx=0, dy=1)
    def moveSouth(self):
        self.move(dx=0, dy=-1)
    def moveEast(self):
        self.move(dx=1, dy=0)
    def moveWest(self):
        self.move(dx=-1, dy=0)
    def whereAmI(self):
        print fla.con_gray(world.room_exists(self.locationX, self.locationY).intro_text())
        #print "I'm in ({},{})".format(self.locationX, self.locationY)
    def room(self):
        return world.room_exists(self.locationX, self.locationY)
    def insult(self):
        print read.read_random_line(self.runTime['insults'])
    def investigate(self):
        print fla.con_gray(world.room_exists(self.locationX, self.locationY).extended_text())

    def use(self, itemName): #TODO
        item = self.hasItemInInventory(itemName)
        if item:
            item.modifyPlayer()
        else:
            print fla.con_gray("I don't have that")
    def attack(self, weapon, enemy):
        if hasItemInInventory(weapon.name):
            enemy.health -= hasItemInInventory(weapon.name).damage
        if enemy.isAlive():
            print ("\n{} HAHA, I have {} health left!!!\n").format(enemy.name, enemy.health)
        else:
            print "Ugggfhhhh...."
    def say (self, phrase):
        print fla.con_gray(phrase)
    def take(self, item):
        room = world.room_exists(self.locationX, self.locationY)
        if room.item.name.upper() == item.upper() :
            if not self.hasItemInInventory(item):
                self.inventory.append(room.item)
                print fla.con_gray("""I now have """ + room.item.name)
            else:
                print fla.con_gray('I can\'t take more of that')

        else:
            print fla.con_gray(self.insult + """ , I can't take that!""")
    def surrender(self):
        print fla.con_gray("""I give up...""")
        exit()
    def help(self): #TODO
        print fla.con_gray("NOOB")
    def status(self):
        print self
    def cry(self):
        print self



#player = Player("Odin")
#print player.hasItemInInventory("Gun").damage
#print player.isAlive()
