# --- Day 5: Binary Boarding ---
# https://adventofcode.com/2020/day/5

# The first 7 characters will either be F or B; these specify exactly one of the 128 rows on the plane
# (numbered 0 through 127).  Each letter tells you which half of a region the given seat is in.

# FBFBBF:
# Start by considering the whole range, rows 0 through 127.
# F means to take the lower half, keeping rows 0 through 63.
# B means to take the upper half, keeping rows 32 through 63.
# F means to take the lower half, keeping rows 32 through 47.
# B means to take the upper half, keeping rows 40 through 47.
# B keeps rows 44 through 47.
# F keeps rows 44 through 45.
# The final F keeps the lower of the two, row 44.FRLR

filename = "Day05.txt"
with open(filename) as f:
    lines = f.read()

existingrows = []       # to store all rows
rowset = set()          # set to store all existing rows (no duplicates)
existingseats = []      # store all seats

tests = lines.split('\n')         # to separate the passports
print(tests[0])

maxID =0
seatIDs = []

for i in range(len(tests)):

    string = tests[i]
    row = [0, 127]
    print(row)

    # starting rows:
    if string[0] == "F":
        row = [0, 63]
    elif string[0] == "B":
        row = [64, 127]

    print("0")
    print(string[0])
    print(row)

    j = 1

    for i in range(1, 7):
        print(i, string[i])
        if string[i] == "F":
            # Lower row[1] (max pos):
            row[1] = row[1] - int(32/j)
        elif string[i] == "B":
            # Lower row[0] (low pos):
            row[0] = row[0] + int(32/j)
            # row = row
        print(row)
        j = j*2

    if row[0] == row[1]:
        finalrow = row[0]
    else:
        print("ERROR")

    print(finalrow)
    print("APPENDED")
    existingrows.append(finalrow)
    rowset.add(finalrow)

    seat = [0, 7]
    k = 1

    # seat column 0 to 7
    for i in range(7,10):
        print(i, string[i])
        if string[i] == "L":
            # Lower row[1] (max pos):
            seat[1] = seat[1] - int(4 / k)
        elif string[i] == "R":
            # Lower row[0] (low pos):
            seat[0] = seat[0] + int(4 / k)
            # row = row
        print(seat)
        k = k*2

    if seat[0] == seat[1]:
        finalseat = seat[0]
        print("seat0", seat[0])
        print("seat1", seat[1])
    else:
        print("ERROR")
        print("seat0", seat[0])
        print("seat1", seat[1])

    print("Append", finalseat)
    existingseats.append(finalseat)

    seatID = finalrow *8 + finalseat
    if seatID > maxID:
        maxID = seatID

    print("row = ", finalrow, "seat = ", finalseat)
    print(seatID)
    seatIDs.append(seatID)

print(maxID)

print("Checking for empty seat:")

print(seatIDs)
print(min(seatIDs))
print(max(seatIDs))

for i in range(min(seatIDs), max(seatIDs)):
    if i in seatIDs:
        pass
    else:
        print("Missing Seat ID: ", i)










