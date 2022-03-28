from itertools import product

n = int(input())

lst = []
for i in range(0, n):
    lst.append(int(input()))

index = 0


for value in lst:
    
    count = 0
    
    for k in range(1, value + 1):
        for i in product([1,2,3], repeat=k):
            temp = 0

            for j in i:
                temp += j
            
            if temp == value:
                count += 1
    
    print(count)