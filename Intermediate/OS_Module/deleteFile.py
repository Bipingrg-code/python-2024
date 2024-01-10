import os
# path = "text.txt"

# try:
#     os.remove(path)

# except FileNotFoundError:
#     print(path + "File not found.!")

# remove directory
path_dir = "new"

try:
    os.rmdir(path_dir)
except FileNotFoundError:
    print("File was not found")
except PermissionError:
    print('You do not have a permission')
else:
    print(path_dir + "was deleted successfully.!")
