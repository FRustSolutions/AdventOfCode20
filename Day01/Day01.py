# https://adventofcode.com/2020/day/1

filename = "numbers.txt"

with open(filename) as f:
    lines = [line.rstrip() for line in f]   #gets rid of new lines in txt
print(lines)
print(len(lines))


for x in range(len(lines)):
    a = int(lines[x])
    for y in range(len(lines)):
        b = int(lines[y])
        for z in range(len(lines)):
            c = int(lines[z])
            d = a + b + c

            if d == 2020:
                if x != y !=z: # make sure we are not adding the same number multiple times
                    print('c=',c)
                    print('a=',a)
                    print('b=',b)
                    print('Add to a sum of: ',d)

                    print('Final result a x b x c=', a*b*c)
                    exit()

