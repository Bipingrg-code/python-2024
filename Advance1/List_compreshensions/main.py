# list comprehension = a way to create a new list with less syntax can mimic certain lambda function, easier to read
# list = [expression (if/else) for item in iterable if conditional]

# import pdb
# basic list iterable
squares = []  # create an empty list

for i in range(1, 11):  # create a for loop
    # pdb.set_trace()
    squares.append(i * i)  # define what each loop iteration should do

# print(squares)

# list comprehension
super_hero = [i*i for i in range(1, 11)]
# print(super_hero)


students = [11, 22, 32, 43, 25, 28, 31, 29, 36, 17, 39]

# pass_students = list(filter(lambda x: x >= 20, students))
pass_students = [i for i in students if i >= 20]
average_students = [i for i in students if i >=20 and i <= 30]
failed_students = [i if i >= 20 else "failed" for i in students]


print(pass_students)
print(average_students)
print(failed_students)