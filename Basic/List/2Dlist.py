# 2d list == list of lists

frontend = ["javascript", "react", "anguler"]
backend = ["node", "django", "php", "rust"]
fullstack = ["python", "wordpress"]

developer = [frontend, backend, fullstack]
print(developer[0][1])
developer[0].append("vue")

print(developer)

developer.append(["devops", "designer"])

# for i in developer:
#     print(i)

# print(developer)
