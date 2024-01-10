import os
source = "test.txt"

destination = "/home/bipingrg/Desktop/test.txt"

try:
    if os.path.exists(destination):
        print("Theres is already a file there.!")
    else:
        os.replace(source, destination)
        print(source + " was moved")

except FileNotFoundError:
    print(source + "File not found.!")
