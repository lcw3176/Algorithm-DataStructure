def solution(id_list, report, k):
    dic = {}
    answer = [0 for i in range(len(id_list))]
 
    for i in report:
        from_user, to_user = i.split(" ")
        
        if to_user not in dic:
            dic[to_user] = []
                
        if from_user in dic[to_user]:
            continue
        
        dic[to_user].append(from_user)

    for i in dic:
        if len(dic[i]) >= k:
            for j in dic[i]:
                answer[id_list.index(j)] += 1
 
    return answer