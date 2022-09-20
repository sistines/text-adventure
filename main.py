author = "Sistines"


class Entity:
    def __init__(self, health, dmg):
        self.health = health
        self.dmg = dmg


class Player(Entity):
    def __init__(self):
        super().__init__()


print(f"{author}'s Text Adventure!")
