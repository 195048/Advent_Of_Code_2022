lines = []
with open("C:\\Users\\saidi\\Desktop\\Advent_Of_Code_2022\\day_four\\1.txt", "r") as input:
    for line in input:
        lines.append((line.strip()))


def contains(A,B) : 
    A = A.split("-")
    B = B.split("-")
    if int(A[0]) <= int(B[0]) and int(A[1]) >= int(B[1]) :
        return True
    elif int(B[0]) <= int(A[0]) and int(B[1]) >= int(A[1]) : 
        return True
    return False

def partial_overlap(A,B): 
    if contains(A,B) : 
        return True
    A = A.split("-")
    B = B.split("-")
    if int(A[0]) <= int(B[0]) and int(A[1]) >= int(B[0]) :
        return True
    elif int(B[1]) >= int(A[0]) and int(B[1]) <= int(A[1]) : 
        return True
    return False

    
score = 0
for line in lines : 
    pairs = line.split(",")
    range1 = pairs[0]
    range2 = pairs[1]
    print(line)
    if partial_overlap(range1,range2): 
        score += 1

print(score)