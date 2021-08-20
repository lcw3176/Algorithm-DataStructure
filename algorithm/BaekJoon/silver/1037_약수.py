_ = input()
lst = list(map(int, input().split(" ")))
lst.sort()
print("{0}".format(lst[0] * lst[-1]))