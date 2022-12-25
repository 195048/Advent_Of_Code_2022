lines = []
with open("C:\\Users\\saidi\\Desktop\\Advent_Of_Code_2022\\day_three\\1.txt", "r") as input:
    for line in input:
        lines.append((line.strip()))


def getPriority(letter) : 
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return alphabet.rfind(letter) + 1

def process_line(line) : 
    half1 = line[:len(line)//2]
    half2 = line[len(line)//2:]
    common_item = (set(half1) & set(half2)).pop() # Thanks Google
    return getPriority(common_item)

score = 0
for line in lines : 
    process_line(line) 
    score += process_line(line)

print(score)