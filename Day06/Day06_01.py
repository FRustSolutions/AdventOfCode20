# --- Day 6: Custom Customs ---
# https://adventofcode.com/2020/day/6


# Example group:
# abcx
# abcy
# abcz
# In this group, there are 6 questions to which anyone answered "yes":
# a, b, c, x, y, and z. (Duplicate answers to the same question don't count extra; '
# each question counts at most once.)


filename = "Day06.txt"
with open(filename) as f:
    lines = f.read()

tests = lines.split('\n\n')         # Groups are split by \n\n
print(tests)
# print(tests[1])

totalyes = 0

# Count the number of unique elements for each group:
for i in range(len(tests)):
    print(i)
    # print(tests[i])
    mystring = "".join(tests[i])        # convert groups to string to get rid of \n
    mychars2 = mystring.split("\n")      # split each char:
    # print(mychars)
    mystring2 = "".join(mychars2)
    print(mystring2)
    mychars = list(mystring2)


    set1 = set(mychars)
    print(set1)
    yescounter = (len(set1))
    print(yescounter)

    totalyes = totalyes + yescounter

print("Total number of yes on unique questions: ", totalyes)


