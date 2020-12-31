# https://adventofcode.com/2020/day/2
# Check if password is valid according to pw policy

# 1-3 a: abcde
# 1-3 b: cdefg
# 2-9 c: ccccccccc
# Each line gives the password policy and then the password.
# The password policy indicates the lowest and highest number of times a given letter must appear for the password to be valid.
# For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.

# read .txt file inputs separated by [space], save the three relevant variables

filename = "Day02.txt"
with open(filename) as f:
    lines = [line.rstrip() for line in f]   # gets rid of new lines in txt
print(lines)
print(len(lines))

# initialise counters:
correct = 0
wrong =0

# Read out the values for the three different properties (amount of letters needed, letter, password:
for i in range (len(lines)):
    # print(i)
    section= lines[i].split()   # splits lines into sections separated by commas
    print(section)              # prints out each passcode section, incremented in loop

    amount = section[0]         # the first part of the section is the amount for the password policy
    amount=amount.split("-")    # splits the min and max numbers
    print(amount)
    min = int(amount[0])        # now we have separate int values we can use
    max = int(amount[1])
    # print(max)

    character = section[1]      # second part of section is the required char
    character = character[0]    # this gets rid of the :
    print(character)            # leaves just the singe char

    passcode = section[2]       # last part of section is the actual passcode
    print(passcode)


    # Check if passcodes meet criteria from part 1:
    counter = 0;
    for j in range (len(passcode)):
        if passcode[j] == character:        # runs through passcode and counts relevant characters
            counter = counter + 1
            print(counter)
    if min <= counter <= max:                   # checks if enough characters were counted
        correct = correct + 1
    else:
        wrong = wrong + 1

print("Number of correct passcodes: ", correct)
print("Number of faulty passcodes: ", wrong)