
class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

class car:

    alive = False
    def speak(self):
        print("Honk!")


animals = [Dog(), Cat(), car()]

for animal in animals:
    animal.speak()
    print(animal.alive)
