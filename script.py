"""2) variables types
three type assignment"""

# assign the following types 
import os, sys


name =  # str -- string

age =   # int -- integer 

decimal = # float --  float



if __name__ == "__main__":  
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
        out.write(l)
        out.close()
    except:
        pass
  

