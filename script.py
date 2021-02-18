"""2) variables types
three type assignment"""

# assign the following types 
import os, sys, json, importlib


#name =  # str -- string

#age =   # int -- integer 

#decimal = # float --  float

var1 = 100


import os
import json
import sys
import importlib
sys.path.append(os.environ.get('USER_CODE_DIR'))

results = []

try:
    userscript = importlib.import_module('script2')
    assert userscript.var1 == 100, "variable1 should be set as 100"
    # test passed
    print("Test passed")
    results.append(True)
except:
    # test failed
    print("Your test failed", sys.exc_info())
    results.append(False)


# append result to file
f = open(os.environ.get('UNIT_TEST_OUTPUT_FILE'), "w")
f.write(json.dumps(results))
f.close()
  

