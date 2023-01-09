array=open("C:\\Users\\saidi\\Desktop\\Advent_Of_Code_2022\\day_seven\\1.txt","r").read().splitlines()

from collections import defaultdict as dd
from math import inf


total_disk=70000000
free_disk=30000000
home_space=48690120 # Gotten from 7.1
required=total_disk-home_space
required=free_disk-required
sizes=dd(list)
dic={}
files=[]
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
            sizes["".join(files)].append("".join(files)+i.split()[1])
            dic["".join(files)+i.split()[1]]=int(i.split()[0])



from time import sleep

t=0
ans = inf
def d(size,directory):
    global t
    global ans
    if directory in dic.keys():return dic[directory]
    for i in sizes[directory]:
        size += d(0,i)
    if size >= required:ans=min(ans,size)
    return size

d(0,"/")


print(ans)