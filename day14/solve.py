puzzle_input = list(map(list,open("data.txt", "r").read().rstrip().splitlines()))

#un peu de redondance pour les mouvements mais ça va plus vite
def move_north() :
    for i,line in enumerate(puzzle_input) :
        for j in range(len(line)) :
            if line[j] == 'O' :
                #search for new place
                for k in range (i-1,-1,-1) : 
                    if puzzle_input[k][j] in '#O' : 
                        puzzle_input[i][j] = '.'
                        puzzle_input[k+1][j]= 'O'
                        break
                    elif k == 0 and puzzle_input[k][j] == '.' :
                        puzzle_input[i][j] = '.'
                        puzzle_input[k][j]= 'O'

def move_west() :
    for i in range(len(puzzle_input[0])) :
        for j in range(len(puzzle_input)) :
            if puzzle_input[j][i] == 'O' :
                #search for new place
                for k in range (i-1,-1,-1) : 
                    if puzzle_input[j][k] in '#O' : 
                        puzzle_input[j][i] = '.'
                        puzzle_input[j][k+1]= 'O'
                        break
                    elif k == 0 and puzzle_input[j][k] == '.' :
                        puzzle_input[j][i] = '.'
                        puzzle_input[j][k]= 'O'

def move_south() :
    for i in range(len(puzzle_input)-1,-1,-1) :
        for j in range(len(puzzle_input[0])) :
            if puzzle_input[i][j] == 'O' :
                #search for new place
                for k in range (i+1,len(puzzle_input)) : 
                    if puzzle_input[k][j] in '#O' : 
                        puzzle_input[i][j] = '.'
                        puzzle_input[k-1][j]= 'O'
                        break
                    elif k == len(puzzle_input)-1 and puzzle_input[k][j] == '.' :
                        puzzle_input[i][j] = '.'
                        puzzle_input[k][j]= 'O'

def move_east() :
    for i in range(len(puzzle_input[0])-2,-1,-1) :
        for j in range(len(puzzle_input)) :
            if puzzle_input[j][i] == 'O' :
                #search for new place
                for k in range (i+1,len(puzzle_input[0])) : 
                    if puzzle_input[j][k] in '#O' : 
                        puzzle_input[j][i] = '.'
                        puzzle_input[j][k-1]= 'O'
                        break
                    elif k == len(puzzle_input[0])-1 and puzzle_input[j][k] == '.' :
                        puzzle_input[j][i] = '.'
                        puzzle_input[j][k]= 'O'

def cycle():
    move_north()
    move_west()
    move_south()
    move_east()

def convert_str(input) :
    return ''.join(''.join(line) for line in input)


res1 = 0
move_north()
for index,line in enumerate(puzzle_input) :
    res1 += line.count('O') * (len(puzzle_input)-index)
print("part 1 : ",res1)

#reinit for part 2
puzzle_input = list(map(list,open("data.txt", "r").read().rstrip().splitlines()))
olds = {convert_str(puzzle_input):0} #on stocke les anciennes iterations
index = 0
loop = 0
while index < 1000000000 :
    if not loop :
        cycle()
        index += 1
        if convert_str(puzzle_input) in olds :#on cherche une boucle qui se repète
            stop = index
            start = olds[convert_str(puzzle_input)]
            loop = stop - start
        else :
            olds[convert_str(puzzle_input)] = index
    elif index + loop < 1000000000 : #une fois la boucle trouvée on s'en sert pour passer des cycles
        index += (1000000000 - index)//loop * loop
    else :#puis on termine
        cycle()
        index +=1
        
res2 = 0
for index,line in enumerate(puzzle_input) :
    res2 += line.count('O') * (len(puzzle_input)-index)
print("part 2 : ",res2)