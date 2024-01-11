class Person:

    name = None
    age = None
    address = None
    email = None

    def __init__(self, name, age, address, email):
        self.name = name
        self.age = age
        self.address = address
        self.email = email

    def coder(self):
        print("He is a coder.!")

    def play_football(self):
        print(self.name + "plays football.")

    def greet(self):
        print("Hello Namaste. my name is"+self.name+" and i am " + str(self.age) +
              " years old.!from " + self.address + "you can reach me out " + self.email)
