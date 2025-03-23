# Inheritance = Allows a class to inherit attributes and methods from another class
#           Helps with code reusability
#           class Child(Parent)

class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal): #inherits attributes and methods from Animal
    def speak(self):
        print(f'{self.name}:"WOOF" ')

class Cat(Animal):
    def speak(self):
        print(f'{self.name}:"MEOW" ')

class Mouse(Animal):
    def speak(self):
        print(f'{self.name}:"SQUEAK" ')

dog = Dog("Scooby")
cat = Cat("Garfield")
mouse = Mouse("Jerry")

print(dog.name)
print(dog.is_alive)
dog.eat()
dog.sleep()
dog.speak()

print()

print(cat.name)
print(cat.is_alive)
cat.eat()
cat.sleep()
cat.speak()

print()

print(mouse.name)
print(mouse.is_alive)
mouse.eat()
mouse.sleep()
mouse.speak()