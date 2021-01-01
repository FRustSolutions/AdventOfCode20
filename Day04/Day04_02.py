# --- Day 4: Passport Processing ---
# https://adventofcode.com/2020/day/4

# passport data in batch files: key-value pairs
# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.

# Passports have 8 fields, but cid field is optional

# example for complete passport data:
# ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183cm
# but missing cid would be valid too

# passport data is separated with empty lines in .txt


filename = "Day04.txt"
with open(filename) as f:
    lines = f.read()

tests = lines.split('\n\n')         # to separate the passports
print(len(tests))

valid = 0
invalid = 0

for i in range(len(tests)):

    # reset for each passport:
    eyecolor = 0
    birthyear = 0
    issueyear = 0
    exyear = 0
    heightcm = 0
    heightin = 0
    haircolor = 0
    passid = 0

    currentvalid = 0

    print(tests[i])

    # Check if all 7 necessary fields are included:
    if "byr" in tests[i] and "iyr" in tests[i] and "eyr" in tests[i] and "hgt" in tests[i] and "hcl" in tests[i] and "ecl" in tests[i] and "pid" in tests[i]:
        # print('Passport ', i, ' is valid')
        # valid = valid +1

        # Check if each fields meets its requirements:
        # ECL:
        ecli = tests[i].find("ecl")
        eyecolor = tests[i][ecli+4] + tests[i][ecli+5] + tests[i][ecli+6]
        if eyecolor == "amb" or eyecolor == "blu" or eyecolor == "brn" or eyecolor == "gry" or eyecolor == "grn" or eyecolor == "hzl" or eyecolor == "oth":
            # BYR:
            ecli = tests[i].find("byr")
            birthyear = tests[i][ecli + 4] + tests[i][ecli + 5] + tests[i][ecli + 6] + tests[i][ecli + 7]
            if 1920 <= int(birthyear) <= 2002:
                # IYR:
                ecli = tests[i].find("iyr")
                issueyear = tests[i][ecli + 4] + tests[i][ecli + 5] + tests[i][ecli + 6] + tests[i][ecli + 7]
                if 2010 <= int(issueyear) <= 2020:
                    # EYR:
                    ecli = tests[i].find("eyr")
                    exyear = tests[i][ecli + 4] + tests[i][ecli + 5] + tests[i][ecli + 6] + tests[i][ecli + 7]
                    if 2020 <= int(exyear) <= 2030:
                        # HGT:
                        ecli = tests[i].find("hgt")
                        if tests[i][ecli + 6] == 'i':
                            heightin = tests[i][ecli + 4] + tests[i][ecli + 5]
                        elif tests[i][ecli + 7] == 'c':
                            heightcm = tests[i][ecli + 4] + tests[i][ecli + 5] + tests[i][ecli + 6]
                        if 59 <= int(heightin) <= 76 or 150 <= int(heightcm) :
                            # HCL:
                            ecli = tests[i].find("hcl")
                            haircolor = tests[i][ecli + 4] + tests[i][ecli + 5] + tests[i][ecli + 6] + tests[i][ecli + 7] + tests[i][ecli + 8] + tests[i][ecli + 9] + tests[i][ecli + 10]
                            hairset = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f'}
                            if haircolor[0] == "#" and (haircolor[1] in hairset) and (haircolor[2] in hairset) and (haircolor[3] in hairset) and (haircolor[4] in hairset) and (haircolor[5] in hairset):
                                # PID:
                                ecli = tests[i].find("pid")
                                passid = tests[i][ecli + 4] + tests[i][ecli + 5] + tests[i][ecli + 6] + tests[i][ecli + 7] + tests[i][ecli + 8] + tests[i][ecli + 9] + tests[i][ecli + 10] + tests[i][ecli + 11] + tests[i][ecli + 12]
                                intset = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
                                if passid[0] in intset and passid[1] in intset and passid[2] in intset and passid[3] in intset and passid[4] in intset and passid[5] in intset and passid[6] in intset and passid[7] in intset and passid[8] in intset:
                                    print('Passport ', i, ' is valid')
                                    currentvalid = 1
                                    valid = valid +1

    if currentvalid == 0:
        print('Passport ', i, ' is invalid')
        invalid = invalid +1

print('Number of valid passports: ', valid)
print('Number of invalid passports: ', invalid)





