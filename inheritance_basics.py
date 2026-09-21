# inheritance_basics.py
# Basic inheritance: a child class inherits everything *and* extends it

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")

    def eat(self):
        print(f"{self.name} is eating")


class Cat(Animal):          # Cat inherits from Animal
    def speak(self):        # override
        print(f"{self.name} says: Meow!")

    def purr(self):         # extra method only Cat has
        print(f"{self.name} is purring...")


class Dog(Animal):
    def speak(self):
        print(f"{self.name} says: Woof!")


if __name__ == "__main__":
    a = Animal("Generic")
    c = Cat("Whiskers")
    d = Dog("Rex")

    a.speak()       # Generic makes a sound
    c.speak()       # Whiskers says: Meow!
    d.speak()       # Rex says: Woof!

    c.eat()         # Whiskers is eating   (inherited from Animal)
    c.purr()        # Whiskers is purring...  (Cat-only)

    # isinstance checks
    print(isinstance(c, Animal))   # True
    print(isinstance(c, Cat))      # True
    print(isinstance(a, Cat))      # False