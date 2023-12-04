puzzle_input = open("data.txt", "r").read().rstrip().splitlines()
clean_input = [line.split(":")[1] for line in puzzle_input]
res1 = 0
res2 = 0

data=[]
for line in clean_input :
    mycards, winnercards = line.split("|")
    mycards, winnercards = mycards.split(), winnercards.split()
    data.append((mycards,winnercards))

cards = [1 for _ in clean_input]

for index,d in enumerate(data) :
    mycards, winnercards = d
    n = len(set(mycards) & set(winnercards))
    if n > 0:
        res1 += 2 ** (n - 1)
    for i in range(n):
        cards[index + i + 1] += cards[index]

res2=sum(cards)

print("part 1 : ",res1)
print("part 2 : ",res2)