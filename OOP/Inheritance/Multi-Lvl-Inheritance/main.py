# multi-level inheritance  =  when a derived (child) class inherits another derived (child ) class

class Organism:

    alive = True


class Animal(Organism):
    def eat(self):
        print("This animal eat.!")


class Dog(Animal):
    def bark(self):
        print("This dog is Bark")


dog = Dog()
print(dog.alive)  # inherits from Organism class
print(dog.eat())  # inherits from Animal class
print(dog.bark())  # inherits from Dog self class
