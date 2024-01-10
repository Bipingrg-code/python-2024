def sum(*nubmer):
    result = 0
    for sum in nubmer:
        result += sum
        print("Sum of total " + str(result))


def subtract(num1, num2):
    result = num1-num2
    print("Subtract of Two number:" + str(result))


def multiple(*numbers):
    result = 0
    for num in numbers:
        result = num * num
        print("Multiple of numbers:" + str(result))


def devided(a, b):
    result = a/b
    print("Divided of Two number is:" + str(result))
