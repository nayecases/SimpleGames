import player



commands = {'north':north, 'south':south, 'east':east, 'west':weast}


class Command:
    def __init__(self, method, name, shortcut, **kwargs):
        self.method = method
        self.name = name
        self.shortcut = shortcut
        self.kwargs = kwargs
    def __str__(self):
        print("Action: {} shortcut: {}").format(self.name, self.shortcut)
