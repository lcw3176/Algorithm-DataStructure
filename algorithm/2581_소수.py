M = int(input())
N = int(input())

answer = []

for i in range(M, N + 1):
    count = 2
    is_prime = True

    while i > count:
        if i % count == 0:
            is_prime = False
            break
        count += 1

    if is_prime and i != 1:
        answer.append(i)

if len(answer) == 0:
    print(-1)
else:
    print(sum(answer))
    print(answer[0])