_ = int(input())
lst = list(map(int, input().split(" ")))
answer = []
is_prime = bool

for i in lst:
    count = 2
    is_prime = True

    while i > count:
        if i % count == 0:
            is_prime = False
            break
        count += 1

    if is_prime and i != 1:
        answer.append(i)

print(len(answer))