# set => collection which is unordered of unique items, unidexed. No duplicate value

person = {"bipin", "swikrit", "gaurav"}

laptops = {"accer", "dell", "hp", "apple", "lenovo"}

phone = {"iphone", "samsung", "oppo", "vivo", "apple"}
person.update(phone)

laptops.update({"samsung", "huwai", "microsoft"})

new_collections = person.union(laptops)
# print(laptops)

# person.add("Abishek")
# person.remove("gaurav")
# # person.clear()

# for i in person:
#     print(i )
# for x in laptops:
#     print(x)

print(phone.difference(laptops))
print(phone.intersection(laptops))

# for i in new_collections:
#     print(i)
