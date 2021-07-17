a, b = map(int, input().split(" "))
big = 0
small = 0
if a >= b:
    big = a
    small = b
else:
    small = a
    big = b

temp = 1
answer = 1
while small >= temp:
    temp += 1
    
    if big % temp == 0 and small % temp == 0:
        big = int(big / temp)
        small = int(small / temp)
        answer *= temp
        temp = 1 


print(answer)
print(int(answer * big * small))