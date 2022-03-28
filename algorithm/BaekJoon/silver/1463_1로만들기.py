n = int(input())

lst = [0 for i in range(1000001)]
lst[1] = 0

for i in range(2, n + 1):
    lst[i] = lst[i - 1] + 1

    if i % 2 == 0:
        lst[i] = min(lst[i], lst[i // 2] + 1)
    if i % 3 == 0:
        lst[i] = min(lst[i], lst[i // 3] + 1)

print(lst[n])