class Animal:

    alive: True
    # name : None

    # def __init__(self, name):
    #     self.name = name

    def eat(self):
        print("This animal eating")

    def sleep(self):
        print("This animal is Sleeping")


class Rabbit(Animal):
    def run(self):
        print("rabbit is running.!")


class Fish(Animal):
    def swim(self):
        print("Fish are swiming.!")


class Dog(Animal):
    def barking(self):
        print("Dog is Barking.!")


