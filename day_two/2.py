lines = []
with open("C:\\Users\\saidi\\Desktop\\Advent_Of_Code_2022\\day_two\\2.txt", "r") as input:
    for line in input:
        lines.append((line.strip()[0],line.strip()[2]))


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


def change_move(opponent,me) :
    lose = {"A": "Z", "B": "X", "C" : "Y"}
    tie = {"A": "X", "B": "Y", "C" : "Z"}
    win = {"A": "Y", "B": "Z", "C" : "X"}
    if me == "X" : 
        return lose[opponent]
    if me == "Z" : 
        return win[opponent]
    else : 
        return tie[opponent]

score = 0

for line in lines : 
    score += calculate_points(line[0],change_move(line[0],line[1]))

print(score)