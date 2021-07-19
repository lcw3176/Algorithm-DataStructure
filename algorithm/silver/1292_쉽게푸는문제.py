A, B = map(int, input().split(" "))
count = 0
lst = []

while len(lst) < B:
    count += 1
    for i in range(0, count):
        lst.append(count)
        
print(sum(lst[A - 1:B]))