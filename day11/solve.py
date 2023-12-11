import itertools

puzzle_input = open("data.txt", "r").read().rstrip().splitlines()
line_without_galaxy = []
column_without_galaxy = []
for index,line in enumerate(puzzle_input) :
    if all([c == '.' for c in line]) :
        line_without_galaxy.append(index)
for j in range(0,len(puzzle_input[0])) :
    if all(line[j]=='.' for line in puzzle_input):
        column_without_galaxy.append(j)

galaxies = [(x,y) for y,line in enumerate(puzzle_input) for x,c in enumerate(line) if c =='#']

def distance(pos1,pos2,expansion) :
    res = 0
    x1,y1 = pos1
    x2,y2 = pos2
    minX,minY=min(x1,x2),min(y1,y2)
    maxX,maxY=max(x1,x2),max(y1,y2)
    res = maxX - minX + maxY - minY
    res += len([1 for line in column_without_galaxy if minX < line < maxX]) * (expansion-1)
    res += len([1 for line in line_without_galaxy if minY < line < maxY]) * (expansion-1)
    return res

galaxy_pairs = list(itertools.combinations(galaxies,2))

res1 = sum(map(lambda x:distance(*x,2),[pair for pair in galaxy_pairs]))
res2 = sum(map(lambda x:distance(*x,1000000),[pair for pair in galaxy_pairs]))

print("part 1 : ",res1)
print("part 2 : ",res2)