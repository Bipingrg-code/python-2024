
def hello():
    print("Hello Namaste Python Developer")


def sumOf_numbers(*numbers):
    sum = 0
    for num in numbers:
        sum += num
    print("Sum of all numbers is: " + str(sum))