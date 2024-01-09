def hello(**kwargs):
    # print("Hello " + kwargs['fname'] + " " + kwargs['lname'])
    for key, value in kwargs.items():
        print(value, end=" ")


hello(fname="bipin", lname="gurung", age=21)
