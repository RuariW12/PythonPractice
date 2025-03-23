# multiple inheritance = inherit from more than one parent class
#           C(A, B)
from tkinter.font import names


# multilevel inheritance = inherit from a parent which inherits from another parent
#           C(B) <- B(A) <- A


#Prey and predator inherit ewverything from animal, and the individual animals trickle down inherit
#   Animal class and Prey and Predator class as well


class Animal:

    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")


class Prey(Animal):
    def flee(self):
        print(f"{self.name} animal is fleeing")

class Predator(Animal):
    def hunt(self):
        print(f"{self.name} animal is hunting")


class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

rabbit= Rabbit("bugs")
hawk = Hawk("tom")
fish = Fish("burt")

rabbit.flee()
hawk.hunt()
fish.flee()
fish.hunt()

rabbit.eat()
fish.eat()

