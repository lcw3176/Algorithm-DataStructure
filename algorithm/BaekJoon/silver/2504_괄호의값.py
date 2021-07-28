lst = list(input())
result_lst = []
temp = 1
result = 0
is_impossible = False

for i in range(0, len(lst)):
    if lst[i] == "(":
        result_lst.append(lst[i])
        temp *= 2

    elif lst[i] == "[":
        result_lst.append(lst[i])
        temp *= 3

    elif lst[i] == ")" and (len(result_lst) == 0 or result_lst[-1] != "("):
        is_impossible = True
        break

    elif lst[i] == "]" and (len(result_lst) == 0 or result_lst[-1] != "["):
        is_impossible = True
        break

    elif lst[i] == ")":
        if lst[i - 1] == "(":
            result += temp
        result_lst.pop()
        temp /= 2
        
    elif lst[i] == "]":
        if lst[i - 1] == "[":
            result += temp
        result_lst.pop()
        temp /= 3

if is_impossible or len(result_lst) != 0:
    print(0)
else:
    print(int(result))