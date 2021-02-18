"""2) variables types
three type assignment"""

# assign the following types 



name =  # str -- string

age =   # int -- integer 

decimal = # float --  float









def main()
    l = []
    out = open(os.environ['OUTPUT_PATH'],'w')
    try:
        if type(name) == str:
            print(f"{name} passed test")
            l.append(True)
        else:
            print(f"{name}: failed test")
            l.append(False)
        if type(age) == int:
            print(f"{age}: passed test")
            l.append(True)
        else:
            print(f"{age}: failed test")
            l.append(False)
        if type(decimal) == float:
            print(f"{decimal}: passed test")
            l.append(True)
        else:
            print(f"{decimal}: failed test")
            l.append(False)
    except:
        pass
    out.write(l)
    out.close()
if __name__ == "__main__":
    main()

  

