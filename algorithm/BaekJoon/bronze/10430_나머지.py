lst = list(map(int, input().split(" ")))
A, B, C = lst[0], lst[1], lst[2]

print((A+B)%C)
print(((A%C) + (B%C))%C)
print((A * B)%C)
print(((A%C) * (B%C))%C)