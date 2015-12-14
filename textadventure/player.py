from items import Gun, Credits
import world
class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = [Credits(30), Gun()]
        self.locationX, self.locationY = world.starting_position
        self.end = False
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)
    def isAlive(self):
        return self.health > 0
    def hasItemInInventory(self, itemName):
        for item in self.inventory:
            if item.name == itemName:
                return item
    def printInventory(self):
        for item in self.inventory:
            print(item, '\n')
    def move(self, dirx, diry):
        self.locationX +=dirx
        self.locationY +=diry
    def moveNorth(self):
        self.move(dx=0, dy=1)
    def moveSouth(self):
        self.move(dx=0, dy=-1)
    def moveEast(self):
        self.move(dx=1, dy=0)
    def moveWest(self):
        self.move(dx=-1, dy=0)

    def attack(self, weapon, enemy):
        if hasItemInInventory(weapon.name):
            enemy.health -= hasItemInInventory(weapon.name).damage
        if enemy.isAlive():
            print("{} HAHA, I have {} health left!!!").format(enemy.name, enemy.health)
        else:
            print "Ugggfhhhh...."


player = Player("Odin")
print player.hasItemInInventory("Gun").damage
print player.isAlive()
