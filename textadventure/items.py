class Item():
    def __init__(self, name, description, value):
        self.value = value
        self.name = name
        self.description = description
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)

class Gold(Item):
    def __init__(self, amount):
        self.amount = amount
        Item.__init__(name = "Gold", description="Booty!!", value = self.amount)

class Weapon(Item):
    def __init__(self, damage):
        self.damage = damage
        Item.__init__(value, name, description)
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)

class Rock(Weapon):
    def __init__(self):
        Weapon.__init__(name = "Rock", description = "..It's a rock", value=0, damage = 5)
class Gun(Weapon):
    def __init__(self):
        Weapon.__init__(name = "Gun", description = "..It's a gun", value=0, damage = 30)
