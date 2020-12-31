# https://adventofcode.com/2020/day/2
# Check if password is valid according to pw policy

# 1-3 a: abcde
# 1-3 b: cdefg
# 2-9 c: ccccccccc
# Each line gives the password policy and then the password.
# The password policy indicates position where the specified character must appear
# For example, 1-3 a means that the password must contain the letter a at position 1 OR 3

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

    # Now to check the passcode criteria:
    min = min-1                # because position otherwise does not match with array starting at 0
    max = max-1
    # Check if passcodes meet criteria from part 2:
    if max <= len(passcode):                                                # make sure the passcode is long enough for max position
        if (passcode[min] == character) or (passcode[max] == character):    # for 2nd part: character needs to be at the specific positions
            print(passcode[min])
            print(passcode[max])
            if passcode[min] == passcode[max]:                              # does not count
                wrong = wrong + 1
            else:
                correct = correct + 1                                       # otherwise passcode meets criteria
    else:
        if passcode[min] == character:                                      # sufficient if the min pos has the char
            correct = correct +1

print("Number of correct passcodes: ",correct)
print("Number of faulty passcodes: ",wrong)

