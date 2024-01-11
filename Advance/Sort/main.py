# sort()  method = used with lists
# sorted() function = used with iterables

students = ["Bipin", "Swikrit", "Samvab", "Jhony"]

super_hero = ("Halk", "Thor", "Captain America", "Tony", "Dr.Stranger")

super_hero_sorted = sorted(super_hero, reverse=True)


students.sort()
# for sort reversed
# students.sort(reverse=True)

for i in students:
    print(i)


for i in super_hero_sorted:
    print(i)
