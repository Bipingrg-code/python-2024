def person():
    # name = input("Enter your name: ")
    age = int(input("Enter your age: "))

    if age == str:
        print("You are not valid entry. Please enter a number.")

    if age >= 18:
        print("You are an adult.")
    elif age <= 14:
        print("You are a child.")
    elif age >= 14 and age <= 18:
        print("You are Teenage")

    else:
        print("Your are not borne yet")
