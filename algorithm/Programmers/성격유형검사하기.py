def solution(survey, choices):
    answer = ""
    dic = {
        'R':0,
        'T':0,
        'C':0,
        'F':0,
        'J':0,
        'M':0,
        'A':0,
        'N':0
    }

    for i in range(len(survey)):
        if choices[i] < 4:
            dic[survey[i][0]] += 4 - choices[i]
        elif choices[i] > 4:
            dic[survey[i][1]] += choices[i] - 4
    
    count = 0
    temp_lst = []
    temp_num_lst = []
    
    for i in dic:
        count += 1
        temp_lst.append(i)
        temp_num_lst.append(dic[i])
        
        if count % 2 == 0:
            
            if temp_num_lst[0] > temp_num_lst[1]:
                answer += temp_lst[0]
            elif temp_num_lst[0] < temp_num_lst[1]:
                answer += temp_lst[1]
            else:
                answer += min(temp_lst[0], temp_lst[1])
                
            count = 0
            temp_lst.clear()
            temp_num_lst.clear()
            
    return answer