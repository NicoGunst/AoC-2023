puzzle_input = open("data.txt", "r").read().rstrip().splitlines()
#only 12 red cubes, 13 green cubes, and 14 blue cubes
maxR = 12
maxG = 13
maxB = 14

res1 = 0
res2 = 0
for line in puzzle_input :
    gameID,gameData = line.split(':') 
    gameID = int(gameID.split(' ')[1])
    gameData = gameData.split(';')
    gameValid = 1;
    gameMaxR=0
    gameMaxG=0
    gameMaxB=0
    for draft in gameData :
        print(draft)
        colors = draft.split(',')
        for c in colors :
            nb,color = c.strip().split(' ')
            if (color=='red' and int(nb)>gameMaxR) :
                gameMaxR = int(nb)
            elif (color=='blue' and int(nb)>gameMaxB) :
                gameMaxB = int(nb)
            elif (color=='green' and int(nb)>gameMaxG) :
                gameMaxG = int(nb)
        #print("r : ",gameMaxR," b : ",gameMaxB," g : ",gameMaxG)
    if (gameMaxR<=maxR and gameMaxB<=maxB and gameMaxG<=maxG):
        res1 += gameValid * gameID
    res2 += gameMaxR * gameMaxB * gameMaxG  
print("part 1 : ",res1)
print("part 2 : ",res2)