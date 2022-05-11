def solution(record):
    dic = {"Enter":"님이 들어왔습니다.", "Leave":"님이 나갔습니다."}
    id_dic = {}
    temp_lst = []
    answer = []
    
    for i in record:
        temp = i.split(" ")
        
        if temp[0] != "Leave":
            id_dic[temp[1]] = temp[2]
        
        if temp[0] != "Change":
            temp_lst.append(temp[0])
            temp_lst.append(temp[1])
            
    for i in range(0, len(temp_lst), 2):
        answer.append(id_dic[temp_lst[i + 1]] + dic[temp_lst[i]]) 
        
    return answer
