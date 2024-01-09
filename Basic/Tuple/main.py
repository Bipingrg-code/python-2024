students = ("Bipin","Male",21,"IT")
print(students.count("Bipin"))
print(students.index('IT'))

for i in students:
    print(i)
    
if "bipin" in students:
    print("He is present")
else:
    print("Absents")