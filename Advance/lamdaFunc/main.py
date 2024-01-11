# lambda function = function written in 1 line using lambda keyword accepts any number of args, but only has one expression.
# think of it as a shortcut
# useful if needed for a short period of time, throw-away


# lambda parameters:expression

# def double(x):
#     return x * 2


# print(double(5))


double  = lambda x: x*2
print(double(5))

multiply = lambda a,b: a * b
print(multiply(3,4))

add = lambda x,y,z: x+y+z
print(add(1,2,3))

full_name = lambda fname,lname:fname+lname
print(full_name("Bipin","Gurung"))
age_check = lambda age:True if age >= 18 else False
print(age_check(18))