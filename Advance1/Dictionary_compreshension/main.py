# dictionary comprehension = create a dictionaries using  an expression
#                            can replace for loops and certain lambda functions


# dictionary = {key: expression for (key,value) in iterable}
# dictionary = {key: expression for (key,value) in iterable if conditional}
# dictionary = {key: (if/else)  for (key,value) in iterable}
# dictionary = {key: function(value) for (key,value) in iterable}

# ----------------------------------------

cities = {"Kathmandu": 32, "Dharan": 39,
          "Pokhara": 28, "Birgunje": 40, "Butwal": 41}

# dictionary change f to celciuse
cities_in_c = {key: round((value-32) * (5/9))
               for (key, value) in cities.items()}
# print(cities_in_c)

new_cites = {"Ithari": "Sunny", "Mustang": "Foggy",
             "Ilam": "Rainy", "Dang": "Average"}
sunny_cities = {key: value for (
    key, value) in new_cites.items() if value == "Sunny"}
# print(sunny_cities)


another_cities = {"Kathmandu": 32, "Dharan": 39,
                  "Pokhara": 28, "Birgunje": 40, "Butwal": 41}

description_cities = {key: ("warm" if value >= 40 else "cold")
                      for (key, value) in cities.items()}
# print(description_cities)


def check_temp(value):
    if value >= 40:
        return "Hot"
    elif value <= 32:
        return "Warm"
    else:
        return "cold"


check_cites_condition = {key: check_temp(
    value) for (key, value) in cities.items()}
print(check_cites_condition)
