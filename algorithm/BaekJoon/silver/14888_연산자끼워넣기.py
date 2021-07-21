from itertools import permutations

_ = int(input())
num_lst = list(map(int, input().split(" ")))
op_int_lst = list(map(int, input().split(" ")))
op_lst = []
temp = ["+", "-", "*" ,"/"]
max_num = 0
min_num = 0
result = 0

for index, element in enumerate(op_int_lst):
    for i in range(element):
        op_lst.append(temp[index])

case_lst = list(permutations(op_lst, len(op_lst)))

for index, op_element in enumerate(case_lst):
    result = num_lst[0]

    for j in range(len(op_lst)):
        if op_element[j] == "+":
            result += num_lst[j + 1]
        elif op_element[j] == "-":
            result -= num_lst[j + 1]
        elif op_element[j] == "*":
            result *= num_lst[j + 1]
        elif op_element[j] == "/":
            result /= num_lst[j + 1]
        result = int(result)

    if index == 0:
        max_num = result
        min_num = result
    else:   
        if result > max_num:
            max_num = result
        
        if result < min_num:
            min_num = result

print(max_num)
print(min_num)