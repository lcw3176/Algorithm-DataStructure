from itertools import combinations

lst = []
for i in range(9):
    lst.append(int(input()))

result = list(combinations(lst, 7))

for i in result:
    temp = 0
    for j in i:
        temp += j
    
    if temp == 100:
        i = sorted(i)
        for k in i:
            print(k)
        break

