class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100, hidden: bool = False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self):
        return f'{{Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}}}'


class Herbivore(Animal):
    def hide(self):
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, target) -> None:
        if isinstance(target, Carnivore):
            return
        if target.hidden:
            return

        target.health -= 50

        if target.health <= 0:
            Animal.alive.remove(target)
