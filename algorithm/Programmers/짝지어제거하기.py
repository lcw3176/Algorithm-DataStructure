def solution(s):
    lst = []

    for i in s:
        if len(lst) > 0 and lst[-1] == i:
            lst.pop()
        else:
            lst.append(i)

    if lst:
        return 0
    else:
        return 1