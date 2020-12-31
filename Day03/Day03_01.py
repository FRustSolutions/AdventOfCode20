filename = "Day03.txt"
with open(filename) as f:
    lines = [line.rstrip() for line in f]   # gets rid of new lines in txt
print(lines)
print(len(lines))

# need to travel through the map: starting top left: always jump to 3 right, 1 down

treecount = 0

# Start:
print(lines[0][0])      # = '.'
print(lines[0][2])      # = '#'   -> [rows][cols]

print(lines[1])
print(len(lines[1]))


# always move right 3 down 1   [+1][+3]:
cols = 0
rows = 0
# and save the character at the position: # = tree or . = no tree
list1 = []

print('Starting the journey')

for i in range(1, len(lines)):
    while(rows < len(lines)):
        print('i', i)
        print('rows', rows, 'cols',  cols)
        pos = lines[rows][cols]
        print(pos)
        list1.append(pos)
        print(list1)

        rows = rows +1
        cols = cols +3

        if cols >= len(lines[0]):   # handle if cols out of range: expand map
            print('Expanding map width (columns)')
            over = cols - len(lines[0])    # checks how far over map we are
            print('Cols', cols)
            print('Over', over)
            if over == 0:
                cols = 0                # if only 1 over start at beginning
            elif over == 1:
                cols = 1
            elif over == 2:
                cols = 2
            else:
                print('Oopsie')

for j in range (0, len(list1)):
    if list1[j] == '#':
        treecount = treecount +1;

print('Number of trees encountered is: ', treecount)



