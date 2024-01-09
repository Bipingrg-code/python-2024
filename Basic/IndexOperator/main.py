# index operator [] = gives access to a sequence's element (str,list,tuples)

name = "bipin gurung"

if (name[0].islower()):
    name = name.capitalize()

first_name  = name[0:3].upper()

last_name =  name[5:].upper()
print(first_name + last_name)