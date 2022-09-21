author = "Sistines"


class Entity:
    def __init__(self, health, dmg):
        self.health = health
        self.dmg = dmg


class Player(Entity):
    def __init__(self):
        super().__init__()

    def move(self, direction):
        pass


class Enemy(Entity):
    def __init__(self):
        super().__init__()


class Game():
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


def main() -> None:
    print(f"Welcome to {author}'s Text Adventure!")
    name = input('Name: ')
    game = Game(name)
    print(f"Welcome {name}")


if __name__ == "__main__":
    main()
