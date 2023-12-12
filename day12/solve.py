import re
import functools
puzzle_input = open("data.txt", "r").read().rstrip().splitlines()

def calculate_group(row) :
    groups = re.findall("#+",row)
    return tuple(map(len,groups))

#first version : bruteforce
# res1 = 0
# for line in puzzle_input :
#     row,condition=line.split(' ')
#     nb_interrogations = row.count('?')
#     nb_combinations = 2 ** nb_interrogations
#     condition = tuple(map(int,condition.split(',')))
#     arrangements = 0
#     #print(row,nb_interrogations,nb_combinations)
#     for i in range(nb_combinations) :
#         binary = list(bin(i)[2:])
#         binary = ['0']*(nb_interrogations-len(binary)) + list(binary)
#         row_list = list(row)
#         iter = 0
#         for j in range(len(row)) :
#             if row_list[j] == '?' :
#                 row_list[j] = '#' if binary[iter]=='1' else '.' 
#                 iter+=1
#         row_combi = "".join(row_list)
#         groups = calculate_group(row_combi)
#         if groups == condition :
#             arrangements += 1
#     res1 += arrangements
# print("part 1 : ",res1)


@functools.cache
def count_arrangements(row, condition):
    if row.startswith("?"):
        first_possibility = row.replace("?", ".", 1)
        second_possibility = row.replace("?", '#', 1)
        return count_arrangements(first_possibility, condition) + count_arrangements(second_possibility, condition)
    if row.startswith("."):
        return count_arrangements(row[1:], condition)
    if row.startswith("#"):
        if len(condition) == 0:
            return 0
        if len(row) < condition[0]:
            return 0
        if '.' in row[0:condition[0]] :
            return 0
        if len(condition) > 1:
            if len(row) < condition[0]+1 or row[condition[0]] == "#":
                return 0
            return count_arrangements(row[condition[0] + 1:], condition[1:])
        else:
            return count_arrangements(row[condition[0]:], condition[1:])
    else :
        if len(condition) == 0:#si plus de condition, l'arrangement est ok
            return 1
        else :
            return 0

res2 = 0
for line in puzzle_input :
     row,condition=line.split(' ')
     row = '?'.join([row] * 5)
     condition = tuple(map(int,condition.split(','))) * 5
     count = count_arrangements(row,condition)
     res2 += count
     #print(row,condition,count)



print("part 2 : ",res2)