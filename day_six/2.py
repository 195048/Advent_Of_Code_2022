lines = []
with open("C:\\Users\\saidi\\Desktop\\Advent_Of_Code_2022\\day_six\\1.txt", "r") as input:
    for line in input:
        lines.append((line.strip()))

def all_unique(list):
    if len(list) == len(set(list)):
        return True
    else:
        return False


def start_Message(input) : 
    
    for i in range(len(input)) : 
        packet = []
        for j in range(14) :
            packet.append(input[i+j])
        print(packet)
        if all_unique(packet) : 
            return (i+14)

input = []
for elem in lines[0] : 
    input.append(elem)        
 

print(start_Message(input))