T = int(input())
lst = []

for i in range(0, T):
    lst.append(int(input()))

for i in lst:
    index = 0
    while i > 0:
        if i % 2 == 1:
            print(index, end=" ")
        index += 1
        i = int(i / 2)
    print()