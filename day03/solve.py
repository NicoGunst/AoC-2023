puzzle_input = open("data.txt", "r").read().rstrip().splitlines()
res1 = 0
res2 = 0

def is_char(char) :
    return char not in '0123456789.'

def adjacents(x,y):
    (x, y) = x,y
    adjacents = [(x+1, y), (x-1, y), (x, y+1), (x, y-1), (x+1, y+1), (x-1, y-1), (x-1, y+1), (x+1, y-1)]
    for x,y in adjacents :
        if x<0 or x>=len(data[0]) or y<0 or y>=len(data) :
            adjacents.remove((x,y))
    return adjacents

def check_arround(x,y):
    char_arround = 0
    for x1,y1 in adjacents(x,y):
        if is_char(data[y1][x1]):
            char_arround +=1
    return char_arround


numbers = []
data = [[char for char in line] for line in puzzle_input]
for y,line in enumerate(data) :
    number = "" 
    number_pos = []
    for x,char in enumerate(line) :
        if char in '0123456789' :
            number += char
            number_pos.append((x,y))
        elif number != "" : #fin du chiffre
            numbers.append((int(number),number_pos,0))
            number = ""
            number_pos = []
    if number != "" : #retour à la ligne
        numbers.append((int(number),number_pos,0))
        number = ""
        number_pos = []

for num,pos,n in numbers :
    for x,y in pos :
        n += check_arround(x,y)
    if n>=1 :
        res1+=num


print("part 1 : ",res1)
print("part 2 : ",res2)