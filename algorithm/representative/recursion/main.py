# 팩토리얼
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return factorial(n - 1)

# 완전 탐색
def search(lst, start, len, word):
    if start == len:
        return False
    
    if word == lst[start]:
        return True

    return search(lst, start + 1, len, word)

# 이진수 구하기
def get_binary(num):
    if num < 2:
        print(num)
        return
    get_binary(num / 2)
    print(num % 2)

# 1부터 n까지의 합
def get_sum(n):
    if n == 1:
        return 1
    return n + get_sum(n - 1)


# 배열의 합
def get_sum_of_arr(arr, start, len):
    if start == len - 1:
        return arr[start]
    
    return arr[start] + get_sum_of_arr(arr, start + 1, len)

# 거듭제곱 구하기
def get_pow(n, x):
    if x == 1:
        return n
    return n * get_pow(n, x - 1)

# 순열 구하기
def permutation(n, r):
    if n == 0 or n == 1 or r == 0:
        return 1
    return n * permutation(n - 1, r - 1)

# 피보나치 수열
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    return fibonacci(n - 2) + fibonacci(n - 1)

