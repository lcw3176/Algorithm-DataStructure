lst = []
max_count = 0

def count_horizontal_block():
    global max_count
    for i in range(0, len(lst)):
        edible = 1
        before_value = lst[i][0]
        for j in range(1, len(lst)):
            if lst[i][j] == before_value:
                edible += 1
            else:
                if max_count < edible:
                    max_count = edible
                edible = 1
            
            before_value = lst[i][j]   
        if max_count < edible:  
            max_count = edible

def count_vertical_block():
    global max_count
    for i in range(0, len(lst)):
        edible = 1
        before_value = lst[0][i]
        for j in range(1, len(lst)):
            if lst[j][i] == before_value:
                edible += 1
            else:
                if max_count < edible:
                    max_count = edible
                edible = 1
                
            before_value = lst[j][i]
        if max_count < edible:  
            max_count = edible

N = int(input())

for i in range(N):
    lst.append(list(input()))

for i in range(0, len(lst)):
    for j in range(0, len(lst) - 1):
        lst[i][j], lst[i][j + 1] = lst[i][j + 1], lst[i][j]
        count_horizontal_block()
        count_vertical_block()
        lst[i][j], lst[i][j + 1] = lst[i][j + 1], lst[i][j] 

        lst[j][i], lst[j + 1][i] = lst[j + 1][i], lst[j][i]
        count_horizontal_block()
        count_vertical_block()
        lst[j][i], lst[j + 1][i] = lst[j + 1][i], lst[j][i]


print(max_count)