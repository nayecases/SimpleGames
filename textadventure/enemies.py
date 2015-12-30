class Enemy():
    def __init__(self, name, description, health, damage):
        self.name = name
        self.description = description
        self.health = health
        self. damage = damage
    def __str__(self):
        return "enemy:{} {} {} ".format(self.name, self.health, self.damage)
    def is_alive(self):
        return self.health > 0
class Reaver(Enemy):
    def __init__(self):
        Enemy.__init__(self, name = "Reaver", description="Human that stared into the void...", health= 100, damage=20)
class Captain(Enemy):
    def __init__(self):
        Enemy.__init__(self, name = "Captain", description="Ching-wah TSAO duh liou mahng that was supposed to help you", health= 50, damage=40)
