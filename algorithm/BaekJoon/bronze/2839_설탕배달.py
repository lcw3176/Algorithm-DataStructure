n = int(input())

answer = -1
temp = 5000

for i in range(0, n + 3, 3):
    for j in range(0, n + 5, 5):
        if i + j == n and i // 3 + j // 5 < temp:
            temp = i // 3 + j // 5

if temp != 5000:
    answer = temp
print(answer)



