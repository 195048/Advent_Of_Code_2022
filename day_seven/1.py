array=open("C:\\Users\\saidi\\Desktop\\Advent_Of_Code_2022\\day_seven\\1.txt","r").read().splitlines()

from collections import defaultdict as dd


sizes=dd(list)
dic={}
files=[]
home_space = 0
for i in array:
    if i[0] =="$":
        if i[2]=="c":
            if i[5]==".":
                files.pop()
            else:#in
                files.append(i[5:])
        else:#ls
            pass
    else:#ls output
        if i[:4] == "dir ":
            sizes["".join(files)].append("".join(files)+i.split()[1])
        else:#file
            home_space += int(i.split()[0])
            sizes["".join(files)].append("".join(files)+i.split()[1])
            dic["".join(files)+i.split()[1]]=int(i.split()[0])



t=0
def d(size,directory):
    global t
    if directory in dic.keys():return dic[directory]
    for i in sizes[directory]:
        size += d(0,i)
    if size <= 100000:t+=size
    return size

d(0,"/")

print(t)
print(home_space)