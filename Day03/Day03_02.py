filename = "Day03.txt"
with open(filename) as f:
    lines = [line.rstrip() for line in f]   # gets rid of new lines in txt
print(lines)
print(len(lines))

# need to travel through the map and count the trees (X): starting top left

treecount = 0       # for each path
totalcount = 0      # for all paths combined
multresult = 1      # for final multiplication result

# now have multiple path options: 1st number: down, 2nd number: right
pathoptions = [(1,1),(1,3),(1,5),(1,7),(2,1)]

print('Starting the journey')

# Loop for different path options:
for k in range (0, len(pathoptions)):
    # insert multiple path options:
    option1 = pathoptions[k]
    print('Changed path options to: ', pathoptions[k])

    cols = 0
    rows = 0
    treecount = 0
    list1 = []

    # loop for each oath through the whole map:
    for i in range(1, len(lines)):
        while(rows < len(lines)):
            pos = lines[rows][cols]
            list1.append(pos)
            # print(list1)

            rows = rows + option1[0]    # incremented depending on current path option
            cols = cols + option1[1]


            if cols >= len(lines[0]):   # handle if cols out of range: expand map width
                # print('Expanding map width (columns)')
                over = cols - len(lines[0])    # checks how far over map we are
                cols = over             # instead of all if statements


    # count the number of trees in the created list:
    for j in range(0, len(list1)):
        if list1[j] == '#':
            treecount = treecount +1;

    print('Number of trees encountered on path', k, 'is: ', treecount)

    totalcount = totalcount + treecount
    multresult = multresult * treecount

print('Total trees encountered from all paths:', totalcount)
print('Our final result of the tree numbers multiplied is: ', multresult)

