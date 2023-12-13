puzzle_input = open("data.txt", "r").read().rstrip().split('\n\n')
res1 = 0
res2 = 0

def is_reflect(pat1,pat2): 
    size = min(len(pat1),len(pat2))
    return pat1[:size] == pat2[:size]

def count_reflection(pattern,old_index=-1) :
    res = 0
    for i in range(1,len(pattern)) :
        if pattern[i-1]==pattern[i] and is_reflect(pattern[i-1::-1],pattern[i:]):
            if i*100 != old_index :
                res += 100 * i
                return res
    pattern = list(zip(*pattern))
    for i in range(1,len(pattern)) :
        if pattern[i-1]==pattern[i] and is_reflect(pattern[i-1::-1],pattern[i:]):
            if i != old_index :#pour partie 2 : on ajoute seulement si différent du premier
                res += i
                return res
    return 0
    

#Part 1
for pattern in puzzle_input :
    pattern = pattern.splitlines()
    res1 += count_reflection(pattern)
print("part 1 : ",res1)

#Part 2
for pattern in puzzle_input :
    pattern = pattern.splitlines()
    part1_answer = count_reflection(pattern)
    res = 0
    for i in range(len(pattern)) :
        for j in range(len(pattern[i])) :
            copy = pattern[:]
            if (pattern[i][j] == '.') :
                copy[i] = pattern[i][:j] + '#' + pattern[i][j+1:]
            else :
                copy[i] = pattern[i][:j] + '.' + pattern[i][j+1:] 
            res = count_reflection(copy,part1_answer)
            if res :
                break
        if res :
                break
    res2+= res

print("part 2 : ",res2)