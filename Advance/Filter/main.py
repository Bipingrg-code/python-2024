# filter() = create a collection of elements from an iterable for which a function return true
# filter(function,iterable)

friends = [("Rachel", 19), ("Monica", 21),
           ("Bipin", 17), ("Jemmy", 24), ("Ronny", 20)]


def age(data): return data[1] >= 18


drink_friends = list(filter(age, friends))

for i in drink_friends:
    print(i)
