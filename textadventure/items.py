class Item():
    def __init__(self, name, description, value):
        self.value = value
        self.name = name
        self.description = description
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)

class Credits(Item):
    def __init__(self, amount):
        self.amount = amount
        Item.__init__(self, name = "Credits", description="Booty!!", value = self.amount)

class Screwdriver(Item):
    def __init__(self):
        Item.__init__(self, name="Screwdriver", description="It's Kaylee's tools...", value = 0)

class Weapon(Item):
    def __init__(self, name, description, value, damage):
        self.damage = damage
        self.value = value
        self.name = name
        self.description = description
        Item.__init__(self, name, description, value)
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)

class Rock(Weapon):
    def __init__(self):
        Weapon.__init__(self, name = "Rock", description = "... It's a rock", value=0, damage = 5)
class Gun(Weapon):
    def __init__(self):
        Weapon.__init__(self, name = "Gun", description = "... It's a gun", value=0, damage = 30)

class Toy(Item):
    def __init__(self):
        Item.__init__(self, name = "Dinosaurs", description="WAAARRRGGH", value = 1000)

class Cake(Item): #TODO
    def __init__(self):
        Item.__init__(self, name = "Cake", description="It's a lie...", value = 5)

class Adrenaline(Item): #TODO
    def __init__(self):
        Item.__init__(self, name = "Adrenaline shot", description="A syringe with a big damn adrenaline dosis", value = 10)


#print Credits( 20)
#print Gun()
