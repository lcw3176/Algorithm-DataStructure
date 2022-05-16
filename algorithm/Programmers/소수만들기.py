from itertools import combinations

def solution(nums):
    answer = 0
    
    for i in combinations(nums, 3):
        temp = i[0] + i[1] + i[2]
        is_prime = True
        
        for j in range(2, temp):
            if temp % j == 0:
                is_prime = False
                break
        
        if is_prime:
            answer += 1
        
    return answer