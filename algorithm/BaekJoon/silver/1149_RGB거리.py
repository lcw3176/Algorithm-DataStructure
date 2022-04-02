# d[1] != d[2]
# d[n] != d[n-1]
# d[i] != d[i - 1], d[i + 1], 단, i >= 2 && i <= n-1

n = int(input())

lst = []

for i in range(n):
    lst.append(list(map(int, input().split(" "))))


for i in range(1, n):
    lst[i][0] = min(lst[i - 1][1], lst[i - 1][2]) + lst[i][0]
    lst[i][1] = min(lst[i - 1][0], lst[i - 1][2]) + lst[i][1]
    lst[i][2] = min(lst[i - 1][0], lst[i - 1][1]) + lst[i][2]
print(min(lst[n - 1]))

    
    
    
# print(sum(lst))
# 3
# 26 40 83
# 49 60 57
# 13 89 99
