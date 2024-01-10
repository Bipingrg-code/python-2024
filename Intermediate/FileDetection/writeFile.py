text = "Hello Python Developer \n Nice to have you \n Happy Coding"
append_text = "Learning Python.!"

# write a file 
with open('test.txt','w') as file:
    file.write(text)
    
with open('test.txt','a') as file:
    file.write(append_text)