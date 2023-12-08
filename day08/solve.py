import math

puzzle_input = open("data.txt", "r").read().rstrip().splitlines()

path = [0 if c=='L' else 1 for c in puzzle_input[0]]
print(path)
dict = {line[0:3] : (line[7:10], line[12:15]) for line in puzzle_input[2:]}
pos = 'AAA'

res1 = 0
while(pos != 'ZZZ' ):
    pos = dict.get(pos)[path[res1%len(path)]]
    res1 += 1

i = 0
start_pos = [k for k in dict.keys() if k.endswith('A')]
steps = [0] * len(start_pos)
while 0 in steps :
    for index, elem in enumerate(start_pos) :
        start_pos[index] = dict.get(start_pos[index])[path[i%len(path)]]
        if start_pos[index].endswith('Z') :
            steps[index] = i+1
    i +=1

res2 = math.lcm(*steps)

print("part 1 : ",res1)
print("part 2 : ",res2)