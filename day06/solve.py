import re
import functools

puzzle_input = open("data.txt", "r").read().rstrip().splitlines()
times = list(map(int,re.findall(r"\d+",puzzle_input[0].split(":")[1])))
targets = list(map(int,re.findall(r"\d+",puzzle_input[1].split(":")[1])))

res1 = 1


#part1
for index,time in enumerate(times) :# pour chaque course
    n = 0
    for i in range(1,time) :
        dist = i *(time-i)
        if(dist>targets[index]) :
            n +=1
    res1 *= n
    n = 0

#Part 2         
res2 = 0
time = int(functools.reduce(lambda a,b : a.strip()+b.strip(),puzzle_input[0].split(":")[1]))
target = int(functools.reduce(lambda a,b : a.strip()+b.strip(),puzzle_input[1].split(":")[1]))
n = 0
print(time,target)
for i in range(1,time) :
    dist = i *(time-i)
    if(dist>target) :
        break

res2 = time - 2 * i + 1

print("part 1 : ",res1)
print("part 2 : ",res2)