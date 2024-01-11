students = [("Bipin", "D", 55), ("Patrick", "B", 67),
            ("Jonney", "A", 90), ("Sandy", "C", 60)]


def grade(grades): return grades[1]


students.sort(key=grade, reverse=True)

# for i in students:
#     print(i)

employee = (("Jonny", "text@gmail.com", "kathmandu", "Backend", 19), ("Patrick", "patrick@tech.com",
                                                                      "Dharan", "Frontend", 23), ("Spongebob", "spnge@test.com", "Austrelia", "Designer", 21))


def age(ages): return ages[2]


employee_sorted = sorted(employee, key=age)

for i in employee_sorted:
    print(i)
