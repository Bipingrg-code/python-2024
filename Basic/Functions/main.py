# def say_name(name):
#     print("My name is" +name)
#     print("Have a nice day.!")


# say_name("Bipin")


# fname = "Bipin"
# lname = "Gurung"


# def hello(fname, lname, age):
#     print("Hello my full name is"+fname + lname)
#     print("my age is" + str(age))


# hello(fname, lname, 21)

# def add_nums(num1, num2):
#     sum = num1 + num2
#     return sum


# sum = add_nums(5, 4)
# print(sum)

def find_sum(*number):
    result = 0
    for num in number:
        result = result + num
        # return result
    print("Sum = ", result)


sum = find_sum(1, 2, 3)
print(sum)
