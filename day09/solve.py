puzzle_input = open("data.txt", "r").read().rstrip().splitlines()

res1 = 0

#Part 1
for line in puzzle_input :
    input = list(map(int,line.split(' ')))
    i = 0
    difference = [input[j]-input[j-1] for j in range(1,len(input))]
    series = [input,difference]
    #phase descente
    while (not all(d == 0 for d in difference)) :
        i+=1
        difference = [series[i][j]-series[i][j-1] for j in range(1,len(series[i]))]
        series.append(difference)
    #phase remontée
    while i > 0 :
        i -= 1 
        series[i].append(series[i][-1] + series[i+1][-1])
    res1 += series[0][-1]

#Part 2
res2 = 0
for line in puzzle_input :
    input = list(map(int,line.split(' ')))[::-1]
    i = 0
    difference = [input[j]-input[j-1] for j in range(1,len(input))]
    series = [input,difference]
    #phase descente
    while (not all(d == 0 for d in difference)) :
        i+=1
        difference = [series[i][j]-series[i][j-1] for j in range(1,len(series[i]))]
        series.append(difference)
    #phase remontée
    while i > 0 :
        i -= 1 
        series[i].append(series[i][-1] + series[i+1][-1])
    res2 += series[0][-1]







print("part 1 : ",res1)
print("part 2 : ",res2)