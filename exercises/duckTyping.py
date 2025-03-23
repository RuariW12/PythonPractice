# "Duck Typing" = Another way to achieve polymorphism besides Inheritance
#       Object must have the minimum necessary attributes/methods
#       "If it looks like a duck and quacks like a duck, it must be a duck."

class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("WOOF")

class Cat(Animal):
    def speak(self):
        print("MEOW")

class Car:
    def horn(self):
        print("HONK")

animals = [Dog(), Cat()]

for animal in animals:
    animal.speak()
    print(animal.alive) #car cant be printed here because it 1.isnt in animals list, 2. if it was it doesnt have a speak method

