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

#Part 2
i = 0
start_pos = [k for k in dict.keys() if k.endswith('A')] #on recupère les pos de départs des fantômes
steps = [0] * len(start_pos) #liste pour stocker les temps mis pour atteindre un Z
while 0 in steps : #tant qu'il reste des fantômes qui ne sont pas arrivés
    for index, elem in enumerate(start_pos) : #pour chaque fantôme,on le fait se déplacer
        start_pos[index] = dict.get(start_pos[index])[path[i%len(path)]]
        if start_pos[index].endswith('Z') :
            steps[index] = i+1
    i +=1

#les fantômes bouclent sur un chemin
#le moment où ils sont en même temps sur leurs Z est le plus petit commun multiple de leurs "step"
res2 = math.lcm(*steps)

print("part 1 : ",res1)
print("part 2 : ",res2)