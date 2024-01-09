try:
    numerator = int(input("Enter the number to divide: "))
    denominator = int(input("Input a number to divided by: "))
    result = numerator / denominator
    print(result)
except ZeroDivisionError as e:
    print(e)
    print("You cant divide by zero! idiot ")
except ValueError as e:
    print(e)
    print("Enter only number ")
except Exception as e:
    print(e)
    print("Something wrong:(")
else:
    print(result)
finally:
    print("this will alyz execute")
