# Prevent a user from creating an object of that class
# a user to override abstract methods in a childe class

# abstract class = a class which contains one or more abstract methods
# abstract object = a method that has a declaration but does not have an implementation

# from abc import ABC, abstractmethod

from abc import ABC, abstractmethod


class Vechile:

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        print("You stop the Vechile.!")


class Car(Vechile):

    def go(self):
        print("You drive a car")

    def stop(self):
        print("You stop the Car")


class SuperBike(Vechile):

    def go(self):
        print("You drive a moter bikes.!")

    def stop(self):
        print("You stop the Super Bike")


vechile = Vechile()
car = Car()
superbike = SuperBike()

print(car.go())
print(vechile.stop())

print(superbike.stop())
