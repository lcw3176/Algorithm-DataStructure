_, _ = map(int, input().split(" "))
blocks = list(map(int, input().split(" ")))
result = 0

for i in range(1, len(blocks)):
    first_wall = 0
    second_wall = 0

    for j in range(i - 1, -1, -1):
        if first_wall < blocks[j]:
            first_wall = blocks[j]

    for k in range(i + 1, len(blocks)):
        if second_wall < blocks[k]:
            second_wall = blocks[k]

    if blocks[i] < min(first_wall, second_wall):
        result += min(first_wall, second_wall) - blocks[i]

print(result)