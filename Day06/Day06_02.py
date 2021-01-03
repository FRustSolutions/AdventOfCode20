# --- Day 6: Custom Customs ---
# https://adventofcode.com/2020/day/6


# You don't need to identify the questions to which anyone answered "yes";
# you need to identify the questions to which everyone answered "yes"!


filename = "Day06.txt"
with open(filename) as f:
    lines = f.read()

tests = lines.split('\n\n')         # Groups are split by \n\n
print(tests)
# print(tests[1])

totalyes = 0
# testset = ["a", "b", "c", "d"]
# sepchars = []
# allyes = []

checkx = []
checkchars = set()
totalcount = 0

# Count the number of unique elements for each group:
for i in range(len(tests)):
    print("Testing groupt number", i)
    # print("i= ", i)
    # print(tests[i])
    mystring = "".join(tests[i])        # convert groups to string to get rid of \n
    answers = mystring.split("\n")      # split each person
    print("answers= ", answers)         # array for group with answers from each person as string

    # split each person into separate characters for each answer:
    x =[[char for char in answers[h]] for h in range(len(answers))]
    print("x= ", x)

    # separate individual persons:
    for j in range(len(x)):
        for char in x[j]:
            checkchars.add(char)

        person = x[j]
        print("person = ", person)

        for char in person:
            print("Char", char)

    print("checkchars: ", checkchars)

    counter = 0
    for char in checkchars:
        print("Char in checkchars: ", char)
        counter = 0
        for k in range(len(x)):
            if char in x[k]:
                counter = counter +1
                print("Counter: ", counter)
            if counter == len(answers):
                print("ITS IN ALL ANSWERS")
                totalcount = totalcount +1


        print("Totalcount= ", totalcount)



