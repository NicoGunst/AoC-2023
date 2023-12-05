import math
import re
from collections import defaultdict

puzzle_input = open("data.txt", "r").read().rstrip().splitlines()
res1 = 0
res2 = 0

chars = { #on recupère la position des caracteres speciaux
    (x, y) for x, line in enumerate(puzzle_input) for y, char in enumerate(line)
    if char not in '0123456789.'
}
adjacents = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

parts_by_chars = defaultdict(list)
for x, line in enumerate(puzzle_input):#pour chaque ligne
    for match in re.finditer(r"\d+", line):#pour chaque nombre
        n = int(match.group(0))
        contours = { #on recupere les cases autours des chiffres
            (x + deltaX, y + deltaY) for deltaX, deltaY in adjacents for y in range(match.start(), match.end())
        }
        if chars & contours: #Part 1 : si un char dans le contour on ajoute la valeur
            res1 += n
        for char in chars & contours:#Part 2 : on ajoute les chiffres autour du char dans le dictionnaire
            parts_by_chars[char].append(n)

print("part 1 : ",res1)

res2 = sum(math.prod(v) for v in parts_by_chars.values() if len(v) == 2)
print("part 2 : ",res2)