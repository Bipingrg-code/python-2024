# zip(*iterable) = aggregate elements from two or more iterable (list,tuples,sets,etc)
#                  create zip object with paired elements store in the tuple for each element


username = ["Bipin", "Gurung", "Developer"]
passwords = ("p@$$w0rd", "abc123", "guest")
login_days = ["1/2/2022", "2/1/2021", "4/9/2023"]


new_users = list(zip(username, passwords, login_days))
print(new_users)

# users = list(zip(username,passwords))

users = dict(zip(username, passwords))

# for i in users:
#     print(i)

for key, value in users.items():
    print(key + " "+value)
print(type(users))
