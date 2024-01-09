# and, or, not

temp = int(input("What is the temp of outside:.?"))
if temp >= 0 and temp <= 30:
    print("the temp is good")
    print("go outside")
elif temp <= 0 or temp >30:
    print("the temp is so bad.")
    print("stay in room")