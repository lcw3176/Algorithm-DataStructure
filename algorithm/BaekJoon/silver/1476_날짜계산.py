E, S, M = map(int, input().split(" "))

E_max = 15
S_max = 28
M_max = 19
count = 1
E_temp = 1
S_temp = 1
M_temp = 1

if E == 1 and S == 1 and M == 1:
    print(1)
else:
    while True:
        if count % E_max == 0:
            E_temp = 1
        else:
            E_temp += 1

        if count % M_max == 0:
            M_temp = 1
        else:
            M_temp += 1

        if count % S_max == 0:
            S_temp = 1
        else:
            S_temp += 1

        count += 1
        if E_temp == E and S_temp == S and M_temp == M:
            break
        
    print(count)