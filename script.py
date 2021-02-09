"""2) variables types
three type assignment"""

# assign the following types 



name =         # str -- string

age =          # int -- integer 

decimal =      # float --  float









def main():
    if type(name) == str:
        print(f"{name}  passed test")
    else:
        print(f"{name}:  failed test")
    if type(age) == int:
        print(f"{age}:  passed test")
    else:
        print(f"{age}:  failed test")
    if type(decimal) == float:
        print(f"{decimal}:  passed test")
    else:
        print(f"{decimal}:  failed test")

if __name__ == "__main__":
    main()
  
'''
// * Make sure that your code does not crash OUTSIDE of try-catch test blocks, otherwise, no test will pass.
// * process.env.USER_CODE_DIR is the directory path of user's code. Use it to import/run user specific code 
// * process.env.PUBLIC_PORT is the publicly accessible port on localhost for user's server. Use it to perform HTTP requests to user server
// * process.env.UNIT_TEST_OUTPUT_FILE is the name of the file where results of UNIT tests should be put
// * The results file should have a JSON array with ONLY "true" or "false" values (booleans) as elements having one-to-one correspondance to challenges you design
'''
