puzzle_input = open("data.txt", "r").read().rstrip().splitlines()
#0 = North, 1 = East, 2 = South, 3 = West
next_pipe = ({'|':{0:2,2:0}, '-':{1:3,3:1},'L':{0:1,1:0},'J':{0:3,3:0},
              '7':{3:2,2:3},'F':{2:1,1:2},'S':{0:{},1:{},2:{},3:{}}, '.':{}})
adjacents = [(0,-1),(1,0),(0,1),(-1,0)]

start_pos = [(x,y) for y,line in enumerate(puzzle_input) for x,c in enumerate(line) if c == 'S'][0]
print("Start position :",start_pos)
x, y = start_pos
loop = [start_pos]
connected_pipes = start_pos
for index,delta in enumerate(adjacents) :
    nextX,nextY,nextDir =(x + delta[0], y + delta[1],(index+2)%4)
    pipe = puzzle_input[nextY][nextX]
    if (nextDir in next_pipe.get(pipe)) :
        connected_pipes =(nextX,nextY,nextDir)
        loop.append((nextX,nextY))
        break

res1 = 1
while(connected_pipes[0:2] != start_pos):
    x,y,dir = connected_pipes
    pipe = puzzle_input[y][x]
    next_dir = next_pipe.get(pipe)[dir]
    deltaX,deltaY = adjacents[next_dir]
    nextX,nextY = x+deltaX,y+deltaY
    connected_pipes = (nextX,nextY,(next_dir+2)%4)
    #if pipe in '|-' :
    loop.append((nextX,nextY))
    res1 +=1

print("Pipe lenght :",res1)
res1 = res1 // 2

def is_point_inside_loop(x, y, loop):
    #Reference: https://www.geeksforgeeks.org/how-to-check-if-a-given-point-lies-inside-a-polygon
    n = len(loop)
    inside = False
    if (x, y) in loop:
        return False
    count = 0
    for i in range(n):
        x1, y1 = loop[i]
        x2, y2 = loop[(i + 1) % n]
        if (y1 > y) != (y2 > y) and x < (x2 - x1) * (y - y1) / (y2 - y1) + x1:
            count += 1
    #
    if count % 2 == 1:
        inside = True

    return inside

res2=0
for i,line in enumerate(puzzle_input) :
    for j,c in enumerate(line) :
        if is_point_inside_loop(j,i,loop) :
            res2 +=1

print("part 1 : ",res1)
print("part 2 : ",res2)