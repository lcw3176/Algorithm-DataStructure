def solution(lines):
    start_lst = []
    end_lst = []
    count = 0
    
    for i in lines:
        date, time, done = i.split(" ")
        hour, minute, second = time.split(":")
        total_millis = 0
        total_millis += ((int(hour) + 1) * 3600 - 3600) * 1000
        total_millis += ((int(minute) + 1) * 60 - 60) * 1000
        total_millis += float(second) * 1000
        start_lst.append(total_millis - float(done.split("s")[0]) * 1000 + 1)
        end_lst.append(total_millis)
    
    for i in range(0, len(lines)):
        before_value = end_lst[i] 
        temp = 0
        for j in range(i, len(lines)):
            if before_value > start_lst[j] - 1000:
                temp += 1
        count = max(count, temp)
        
    return count