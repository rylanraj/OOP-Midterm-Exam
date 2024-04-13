class Pokemon:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.level = 1

        if type(self.name) is not str:
            raise ValueError()

        if type(self.health) is not int:
            raise ValueError()

        if self.name == "":
            raise ValueError()

        if self.health <= 0:
            raise ValueError()

    def level_up(self):
        self.level += 1

    def set_level(self, level):
        self.level = level

    def join(self, arena):
        arena.add(self)


