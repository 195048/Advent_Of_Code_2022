array=open("C:\\Users\\saidi\\Desktop\\Advent_Of_Code_2022\\day_five\\1.txt", "r").read()

array,commands=array.split("\n\n")

array,commands=array.splitlines(),commands.splitlines()

crates=[""]*9


for i in range(len(array)-2,-1,-1):
    for r in range(1,len(array[0]), 4):
        if array[i][r].isupper():crates[r//4]+=array[i][r]



for i in commands:
    a,crate,c,origin,e,destination=i.split()

    crate,origin,destination=int(crate),int(origin),int(destination)
    print(crate,origin,destination)
    origin,destination=origin-1,destination-1

    crates[destination]+=crates[origin][-crate:]
    crates[origin]=crates[origin][:-crate]


t=""
for i in crates:
    try:
        t+=i[-1]
    except:
        pass

print(t)