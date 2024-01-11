#  Duck typing = concept where the class of an object is less important then the methods/attributes
# class type is not checked if minimum methods/attributes are present "If it walks like a duck, and quacks like a duck, then it must be a duck"
class Duck:
    def walk(self):
        print("The duck is walking.")

    def talk(self):
        print("Quack!")


class Chicken:
    def walk(self):
        print("The chicken is walking.")

    def talk(self):
        print("Cluck!")


class Person():

    def catch(self, duck):
        duck.walk()
        duck.talk()
        print("Got's you.!")


duck = Duck()
chicken = Chicken()
person = Person()

# The person can catch a duck or a chicken
person.catch(duck)
