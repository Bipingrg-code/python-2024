# walrus operator :=
# new to Python3.8
# assignment operator aka walrus operator
# assigns value to variables as part of a larger expression


# happy = True
happy = (happy := False) and not happy  # if happy is True, it
# becomes False; otherwise stays False

# foods = list()

# while True:
#     food = input("Enter foods or 'q' to quit: ")
#     if food == "quit":
#         break
#     foods.append(food)

foods = list()

while food := input("What food do you like.?") != "quit":
    foods.append(food)
    
print(foods)
