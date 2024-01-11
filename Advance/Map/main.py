# map() = applies a function to each item in an iterable (list,tupple,etc)

# map(function,iterable)


shoes = [("Nike", 4000),
         ("Jordan", 3500),
         ("Addidas", 3000),
         ("Erick", 4500)]

# convert npr price to dolor


def to_dolor(data): return (data[0], data[1]/132)


shoes_dolor = list(map(to_dolor, shoes))

for i in shoes_dolor:
    print(i)
