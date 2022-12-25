lines = []
with open("C:\\Users\\saidi\\Desktop\\Advent_Of_Code_2022\\day_three\\1.txt", "r") as input:
    for line in input:
        lines.append((line.strip()))


def getPriority(letter) : 
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return alphabet.rfind(letter) + 1

def process_group(group) : 
    common_item = (set(group[0]) & set(group[1]) & set(group[2])).pop()
    return getPriority(common_item)



score = 0
groups = []
group = []
i = 1
for line in lines: 
    group.append(line)
    if i % 3 == 0 : 
        groups.append(group)
        group = []
    i += 1


for group in groups : 
    score += process_group(group)

print(score)
