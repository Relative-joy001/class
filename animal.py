class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("meow!")

class Bird(Animal):
    def speak(self):
        print("tweet!")

dog = Dog("Buddy")
cat = Cat("Whiskers")
bird = Bird("Tweety")

print(dog.name)
print(dog.is_alive)

dog.eat()

dog.sleep()
