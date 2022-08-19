def solution(arr):
    answer = []
    answer.append(arr[0])
    index = 0
    
    for i in arr:
        if i != answer[index]:
            answer.append(i)
            index += 1
    
    return answer