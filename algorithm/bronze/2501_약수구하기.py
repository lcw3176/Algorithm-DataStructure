N, K = input().split(" ")
N = int(N)
K = int(K)

lst = []

for i in range(1, N + 1):
    if N % i == 0:
        lst.append(i)

if len(lst) < K:
    print(0)
else:
    print(lst[K - 1])

