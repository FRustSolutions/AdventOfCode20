filename = "Day03.txt"
with open(filename) as f:
    lines = [line.rstrip() for line in f]   # gets rid of new lines in txt
print(lines)
print(len(lines))

treecount = 0

# Start:
lines[0][0]
print(lines[0][0])

# always move right 3 down 1:
line =0;
position =0;

for linecount in range(11):
    print(linecount)
    for poscount in range(0,11,3):
        print(poscount)
        a = lines[linecount][poscount]
        print(a)
        if a == "#":
            treecount = treecount +1
print(treecount)

