def add(*numbers):
    sum = 0
    numbers = list(numbers)
    numbers[0] = 20
    for i in numbers:
        sum += i

    return sum


print(add(1, 2, 3, 4, 5, 6))
