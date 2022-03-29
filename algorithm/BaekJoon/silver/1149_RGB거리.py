# d[1] != d[2]
# d[n] != d[n-1]
# d[i] != d[i - 1], d[i + 1]

# 2 <= i <= n -1


# n = int(input())

# lst = [0 for _ in range(n + 1)]
# identifier = [0 for _ in range(n + 1)]
# temp_lst = []

# for i in range(0, n):
#     temp_lst = list(map(int, input().split(" ")))

# for i in temp_lst:
#     identifier[i + 1] = temp_lst.index(int(min(temp_lst)))
#     lst[i + 1] = min(temp_lst)

#     if i >= 1 and identifier[i] == identifier[i + 1]:
#         max_index = max(lst[i], lst[i + 1])
#         lst[max_index]
        

#     # if i >= 2 and identifier[i + 1] == identifier[i - 1]:        
#     #     temp_lst[identifier[i + 1]] = 100000
#     #     identifier[i + 1] = temp_lst.index(min(temp_lst))

    
    
    
# print(sum(lst))
# 3
# 26 40 83
# 49 60 57
# 13 89 99
