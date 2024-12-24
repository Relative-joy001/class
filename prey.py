# Multiple inheritance example

class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"The {self.name} eats!")
    
    def sleep(self):
        print(f"The {self.name} sleeps!")

class Prey(Animal):
    def flee(self):
        print(f"The {self.name} flees!")

class Predator(Animal):
    def hunt(self):
        print(f"The {self.name} hunts!")

class Rabbit(Prey):
    pass

class Fox(Predator):
    pass

class Fish(Prey, Predator):
    pass

rabbit = Rabbit("Bunny")
fox = Fox("Foxxy")
fish = Fish("Nemo")

fox.eat()

