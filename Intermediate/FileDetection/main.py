import os

path = "/home/bipingrg/Documents/text"

if os.path.exists(path):
    print("location exists")
    if os.path.isfile(path):
        print("that is a file")
    elif os.path.isdir(path):
        print("that is directory")
else:
    print("location doesnt exists")
