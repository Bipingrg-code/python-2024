# if __main__ == '__main__'

# 1-> model can be run as a standalone program
# 2 -> model is imported from another script and used in that script only.
# 3 -> model can be imported and used by other modules

# python interpreter sets "special variable", one of which is '__name__'
# then python will execute the code found within __main__


def main():
    print("Hello")
    
    
if __name__ =='__main__':
    main()