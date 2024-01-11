# method chaining =  calling multiple methods sequentially each call perform an action on the same object that returns self
class Car:

    def turn_on(self):
        print("You turn on engine")
        return self

    def drive(self):
        print("You start driving.!")
        return self

    def brake(self):
        print("You Brake the car")
        return self

    def turn_off(self):
        print("You stop the engine.!")
        return self


car = Car()

# car.turn_on
car.turn_on().drive().turn_off()
