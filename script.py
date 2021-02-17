
"""
24)  Custom Function with return

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

