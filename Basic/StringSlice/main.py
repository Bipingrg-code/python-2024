name = "Sanjiv Gurung"

first_name = name[0:6]
last_name = name[6:13]

funky_name = name[0:7:3]
reversed_name = name[::-1]

# print(first_name + last_name)
# print(funky_name)
# print(reversed_name)

website = "https://google.com"
website1 = "https://youtube.com.np"

website_slice = slice(8, -4)
website1_slice = slice(8, -7)
print(website[website_slice])
print(website1[website1_slice])
