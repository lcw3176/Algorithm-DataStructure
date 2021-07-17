T = int(input())

for i in range(T):
    lst = list(map(int, input().split(" ")))

    for j in range(0, len(lst)):
        for k in range(j, len(lst)):
            if lst[j] < lst[k]:
                temp = lst[j]
                lst[j] = lst[k]
                lst[k] = temp
    print(lst[2])