lines = []
elves = []
calories = []

with open("C:\\Users\\saidi\\Desktop\\Advent_Of_Code_2022\\day_one\\1.txt", "r") as input:
    for line in input:
        lines.append(line.strip())

elf = []
for elem in lines : 
    if elem == '': 
        elves.append(sum(elf))
        elf.clear()
    else :
        elf.append(int(elem))
    
elves.sort()
print(elves[-1] + elves[-2] + elves[-3] )