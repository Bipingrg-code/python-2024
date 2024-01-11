class Car:

    color = None


class Motercycle:

    brand = None


def change_color(vehicle, color):

    vehicle.color = color

def brand_change(bike, brand):

    bike.brand = brand



car_1 = Car()
car_2 = Car()

change_color(car_1, "Red")
change_color(car_2, "Black")

print(car_1.color)
print(car_2.color)


bike_1 = Motercycle()
bike_2 = Motercycle()


brand_change(bike_1,"Kawasaki")
brand_change(bike_2,"Harly Deversion")

print(bike_1.brand)
print(bike_2.brand)