puzzle_input = open("data.txt", "r").read().split("\n\n")
seeds = list(map(int,puzzle_input[0].split(': ')[1].split(' ')))

seeds_info =[]
for seed in seeds :#pour chaque graine
    seedPos = seed
    for type in puzzle_input[1:] : #pour chaque catégorie
        for section in type.splitlines()[1:] : #pour chaque section
            destination, source, ecart = map(int,section.split())
            if (source <=seedPos < source+ecart) :
                seedPos= seedPos - source + destination
                break
                
    seeds_info.append(seedPos)

res1 = min(seeds_info)

seeds = [[seeds[i],seeds[i]+seeds[i+1]-1] for i in range(0, len(seeds), 2)]
for type in puzzle_input[1:] : #pour chaque catégorie
    i = 0
    while(i < len(seeds)) :#pour chaque liste de graines
        find = False
        start,end = seeds[i]
        for section in type.splitlines()[1:] : #pour chaque section
            destination, source, ecart = map(int,section.split())
            #on travaille uniquement sur les début et fin de range de seed
            if source <= start < (source + ecart) and not find:
            #si premiere seed du range dans cette section
                find = True
                seeds[i][0] = start - source + destination
                if end < source + ecart: #si le range termine dans la section
                    seeds[i][1] = end - source + destination
                else: #si le range sort de la section, on ajoute un range dans la liste
                    seeds[i][1] = destination + ecart - 1 
                    seeds.append([source + ecart, end])
			#idem mais pour la fin		
            elif source <= end < (source + ecart) and not find:
                find = True
                seeds[i][1] = end - source + destination	
                seeds[i][0] = destination
                seeds.append([start, source-1])                
        i+=1
res2 = min(min(seeds))

print("part 1 : ",res1)
print("part 2 : ",res2)