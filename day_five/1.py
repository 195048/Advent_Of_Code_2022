array=open("C:\\Users\\saidi\\Desktop\\Advent_Of_Code_2022\\day_five\\1.txt", "r").read()

array,commands=array.split("\n\n")

array,commands=array.splitlines(),commands.splitlines()


crates=[""]*9


for i in range(len(array)-2,-1,-1):
    for j in range(1,len(array[0]), 4):
        if array[i][j].isupper():crates[j//4]+=array[i][j]



for i in commands:
    a,crate,c,origin,e,destination=i.split()

    crate,origin,destination=int(crate),int(origin),int(destination)
    print(crate,origin,destination)
    origin,destination=origin-1,destination-1

    for r in range(crate):
        crates[destination]+=crates[origin][-1]
        crates[origin]=crates[origin][:-1]


t=""
for i in crates:
    try:
        t+=i[-1]
    except:
        pass

print(t)