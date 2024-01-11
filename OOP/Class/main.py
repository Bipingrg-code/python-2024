from person_class import Person
from car_class import Car

person_1 = Person("Bipin", 21, "Kathmandu", "bipin@gmail.com")
person_2 = Person("Jhon", 24, "USA", "jhon@test.com")

print(person_1.name)
print(person_1.age)
print(person_1.address)
print(person_1.email)

person_1.play_football()
person_1.coder()
person_1.greet()

person_2.play_football()
person_2.greet()


car_1 = Car("Farari",1994,"Black")

print(car_1.model)
car_1.description()
print(car_1.wheels)