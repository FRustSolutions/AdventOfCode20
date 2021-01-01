# --- Day 4: Passport Processing ---
# https://adventofcode.com/2020/day/4

# passport data in batch files: key-value pairs
# 1: byr (Birth Year)
# 2: iyr (Issue Year)
# 3: eyr (Expiration Year)
# 4: hgt (Height)
# 5: hcl (Hair Color)
# 6: ecl (Eye Color)
# 7: pid (Passport ID)
# 8: cid (Country ID)              # optional

# Passports have 8 fields, but cid field is optional

# example for complete passport data:
# ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183cm
# but missing cid would be valid too

# passport data is separated with empty lines in .txt

filename = "Day04.txt"
with open(filename) as f:
    lines = f.read()

tests = lines.split('\n\n')         # to separate the passports

print(tests)
valid = 0

for i in range(len(tests)):
    if "byr" in tests[i] and "iyr" in tests[i] and "eyr" in tests[i] and "hgt" in tests[i] and "hcl" in tests[i] and "ecl" in tests[i] and "pid" in tests[i]:
        print('Passport ', i, ' is valid')
        valid = valid +1
    else:
        ('Nopers')

print('Number of valid passports: ', valid)





