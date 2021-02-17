"""2) variables types
three type assignment"""

# assign the following types 



name =  # str -- string

age =   # int -- integer 

decimal = # float --  float









def main():
    try:
        if type(name) == str:
            print(f"{name} passed test")
            return True
        else:
            print(f"{name}: failed test")
        if type(age) == int:
            print(f"{age}: passed test")
        else:
            print(f"{age}: failed test")
        if type(decimal) == float:
            print(f"{decimal}: passed test")
        else:
            print(f"{decimal}: failed test")
    except:
        pass

if __name__ == "__main__":
    main()

  

