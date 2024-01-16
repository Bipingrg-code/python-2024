
from cryptography.fernet import Fernet

# store a key


def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)


write_key()


# load key
def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close
    return key


key = load_key()
fer = Fernet(key)


# view func


def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            # print(line.rstrip())
            data = line.rstrip()
            user, pwd = data.split("|")
            print("User:", user, " | Password:",
                  fer.decrypt(pwd.encode()).decode())


# add func

def add():
    name = input("Account name: ")
    password = input("Password.: ")

    # open the file and append the password
    with open('password.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(password.encode()).decode() + "\n")


while True:
    mode = input(
        "Would you like to add a new password or view exiting ones (view,add) or q to Quit.:").lower()

    if mode == 'q':
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid Mode:")
        continue
