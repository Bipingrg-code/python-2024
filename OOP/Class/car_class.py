class Car:

    model = None
    year = None
    color = None
    
    wheels =  4 #class variable

    def __init__(self, model, year, color):
        self.model = model  # instance variable
        self.year = year  # instance variable
        self.color = color  # instance variable

    def description(self):
        print("This is a super car")

    def drive(self):
        print(self.model + "This cas is drive")
