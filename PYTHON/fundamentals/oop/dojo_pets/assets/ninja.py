

class Ninja:

    ninjas = []

    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.pet_food = pet_food
        self.pet = pet
        if treats < 0:
            print("You can't have a negative number of treats!")
        else:
            self.treats = treats
        Ninja.ninjas.append(self)

    def walk(self):
        self.pet.play()
        print(
            f"{self.first_name} {self.last_name} is walking {self.pet.name}!")
        return self

    def feed(self, treat_amount):
        if treat_amount > self.treats:
            print('Not enough treats!')
        else:
            self.pet.eat()
            self.treats -= treat_amount
            print(
                f"{self.first_name} {self.last_name} fed {self.pet.name} {treat_amount} {self.pet_food}s!")
        return self

    def bathe(self):
        self.pet.noise()
        return self
