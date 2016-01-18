from items import Gun, Credits
from random import randint

import world

insults = ["Shun-SHENG duh gao-WAHN (Holy Testicle Tuesday)", "Da-shiang bao-tza shr duh lah doo-tze (The Explosive Diarrhea of an Elephant)",
            "Tai-kong suo-yo duh shing-chiou sai-jin wuh duh pee-goo ( Shove All the Planets in the Universe Up my Ass)",
            "Wuh duh ma huh tah duh fong kwong duh wai shung (Holy Mother of God and All Her Wacky Nephews)",
            "Gao yang jong duh goo yang (Motherless Goats of All Motherless Goats)",
            "Huh choo-shung tza-jiao duh tzang-huo (Filthy Fornicators of Livestock)",
            "Gun HOE-tze bee DIO-se (Have a Shit-Throwing Contest with a Monkey)",
            "Ching-wah TSAO duh liou mahng (Frog-Humping Son of a Bitch)",
            "Liou coe shway duh biao-tze huh hoe-tze duh ur-tze (Stupid Son of a Drooling Whore and a Monkey)",
            "Shiong mao niao (Panda Piss)",
            "Go tsao de (Dog Fucking)"
]

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = [Credits(30), Gun()]
        self.locationX, self.locationY = world.starting_position
        self.end = False
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name)
    def isAlive(self):
        if self.health > 0:
            print "All good so far"
        else:
            print "... tell my mother I love her"
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
            print """I can't go there!"""
    def moveNorth(self):
        self.move(dx=0, dy=1)
    def moveSouth(self):
        self.move(dx=0, dy=-1)
    def moveEast(self):
        self.move(dx=1, dy=0)
    def moveWest(self):
        self.move(dx=-1, dy=0)
    def whereAmI(self):
        print world.room_exists(self.locationX, self.locationY).intro_text()
        #print "I'm in ({},{})".format(self.locationX, self.locationY)
    def room(self):
        return world.room_exists(self.locationX, self.locationY)
    def insult(self):
        print insults[randint(0, len(insults)-1)]
    def investigate(self):
        print world.room_exists(self.locationX, self.locationY).extended_text()

    def use(self, itemName): #TODO
        item = self.hasItemInInventory(itemName)
        if item:
            #print item
            if item.specialRoom # HAY QUE HACERLO
        else:
            print "I don't have that"
    def attack(self, weapon, enemy):
        if hasItemInInventory(weapon.name):
            enemy.health -= hasItemInInventory(weapon.name).damage
        if enemy.isAlive():
            print("{} HAHA, I have {} health left!!!").format(enemy.name, enemy.health)
        else:
            print "Ugggfhhhh...."
    def say (self, phrase):
        print phrase
    def take(self, item):
        room = world.room_exists(self.locationX, self.locationY)
        if room.item.name == item :
            if not self.hasItemInInventory(item):
                self.inventory.append(room.item)
            elif:
                print 'I can\'t take more of that'
            print """I now have """ + room.item.name
        else:
            print self.insult + """ , I can't take that!"""
    def surrender(self):
        print """I give up..."""
        exit()
    def help(self): #TODO
        print "NOOB"



#player = Player("Odin")
#print player.hasItemInInventory("Gun").damage
#print player.isAlive()
