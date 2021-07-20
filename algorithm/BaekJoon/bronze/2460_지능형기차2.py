count = 0
max = 0

for i in range(0, 10):
    off, on = map(int, input().split(" "))
    count = count + on - off

    if count >= max:
        max = count

print(max)