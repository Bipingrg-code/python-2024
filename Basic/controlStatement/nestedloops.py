# nested loops 

rows = int(input("how many rowsa.?"))
cols = int(input("how many rows"))
symbols = input("Enter the symbols")

for i in range(rows):
    for j in range(cols):
        print(symbols, end=" ")
        
    print()