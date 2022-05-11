def solution(id_list, report, k):
    filtered_dict = {}
    dic = {}
    answer = [0 for i in range(len(id_list))]
    
    for users in report:
        filtered_dict[users] = 0

    for users in filtered_dict:
        sender, receiver = users.split(" ")
        
        if receiver not in dic.keys():
            dic[receiver] = []
        dic[receiver].append(sender)
    
    for i in dic:
        if len(dic[i]) >= k:
            for j in dic[i]:
                answer[id_list.index(j)] += 1
        
    return answer