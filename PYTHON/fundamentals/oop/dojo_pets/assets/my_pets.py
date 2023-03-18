

class Pet():

    pets = []

    def __init__(self, name, tricks, health, energy, type=''):
        self.name = name
        self.tricks = tricks
        self.health = health
        self.energy = energy
        self.type = type
        Pet.pets.append(self)

    def sleep(self):
        self.energy += 25
        return self

    def eat(self):
        self.energy += 5
        self.health += 10
        return self

    def play(self):
        self.health += 5
        return self

    def noise(self):
        print("We haven't learned how to describe this noise yet :(")
        return self

# Cats


class Cats(Pet):
    def __init__(self, name, tricks, health, energy, type='cat'):
        super().__init__(name, tricks, health, energy)
        self.type = type.lower()

    def noise(self):
        if self.type == 'cat':
            print(self.name, "Meows Loudly")
        else:
            super().noise()
        return self


class Raccoons(Pet):
    def __init__(self, name, tricks, health, energy, type='raccoon'):
        super().__init__(name, tricks, health, energy)
        self.type = type.lower()

    def sleep(self):
        self.energy += 100
        return self

    def eat(self):
        self.energy += 10
        self.health += 15
        return self

    def play(self):
        self.health += 10
        return self

    def noise(self):
        if self.type == 'raccoon':
            print(f"{self.name} says 'Buddy I speak english'")
        else:
            super().noise()
        return self


class Dogs(Pet):
    def __init__(self, name, tricks, health, energy, type='dog'):
        super().__init__(name, tricks, health, energy)
        self.type = type.lower()

    def sleep(self):
        self.energy += 50
        return self

    def eat(self):
        self.energy += 5
        self.health += 15
        return self

    def play(self):
        self.health += 50
        return self

    def noise(self):
        if self.type == 'dog':
            print(self.name, "woof bork")
        else:
            super().noise()
        return self
