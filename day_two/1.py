lines = []
with open("C:\\Users\\saidi\\Desktop\\Advent_Of_Code_2022\\day_two\\1.txt", "r") as input:
    for line in input:
        lines.append((line.strip()[0],line.strip()[2]))

score = 0

def calculate_points(opponent,me) : 
    base_points = {"X": 1, "Y": 2, "Z" : 3}
    tie = {"A": "X", "B": "Y", "C" : "Z"}
    win = {"A": "Y", "B": "Z", "C" : "X"}
    if tie[opponent] == me:
        return 3 + base_points[me]
    elif win[opponent] == me:
        return 6 + base_points[me]
    else : 
        return 0 + base_points[me]
    

for line in lines : 
    score += calculate_points(line[0],line[1])

print(score)


    
