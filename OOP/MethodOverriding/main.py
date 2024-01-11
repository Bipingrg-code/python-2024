class Animal:
    def eat(self):
        print("this animal is eat.!")
        
class Rabbit(Animal):
    def eat(self):
        print('Rabbit eat grass.!')

rabbit = Rabbit()

rabbit.eat()