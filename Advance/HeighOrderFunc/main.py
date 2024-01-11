# Higher Order Function = a function that either:
# (1) takes another function as an argument, or
# (2) returns a new function.
# (In python, functions are also treated as objects)

def loud(text): 
    return text.upper()
def quiet(text):
    return text.lower()

def hello(func):
    text = func("Hello")
    print(text)

hello(loud)
hello(quiet)