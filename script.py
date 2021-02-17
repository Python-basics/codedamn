
"""
24)  Custom Function with return



Finish a function called total...
You are going to loop through a list
to total the number of students in a grade
on the second line write for loop iterating through the variable l (a list)
on the third line of the body which will be indented
increment sub_ttl with the intermediate variable you are using

hint: incrementation should be indented under for loop

Great job!!!!

"""


students = [40,38,24,45,48,32,34]

def total(l):
    sub_ttl = 0     # this is your sub-total starting point 
    for i in students:
        sub_ttl += i
    return sub_ttl


def main():
    try:
        if total(students) == 261:
            print(f"""total: passed test
Total number of students is {total(students)}""")
        else:
            print(f"""total: failed test
got {total(students)}, expected 261""")
    except:
        print("OOps, something went wrong. Try again")


if __name__ == "__main__":
    main()

