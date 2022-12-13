from collections import deque


def bfs(graph, start_lst, visited):
    queue = deque(start_lst)

    for i in start_lst:
        visited[i] = True
    
    count = 0

    while True:
        lst = []
        while queue:
            lst.append(queue.popleft())

        for n in lst:
            if n <= -1 or n >= len(graph) or graph[n] == -1:
                continue

            if not visited[n]:
                visited[n] = True
                graph[n] = 1
            
            if n - 1 >= 0 and n % w != 0 and graph[n - 1] != -1 and graph[n - 1] != 1:
                queue.append(n - 1)
                graph[n - 1] = 1
            
            if n + 1 < len(graph) and (n + 1) % w != 0 and graph[n + 1] != -1 and graph[n + 1] != 1:
                queue.append(n + 1)
                graph[n + 1] = 1
            
            if n - w >= 0 and graph[n - w] != -1 and graph[n - w] != 1:
                queue.append(n - w)
                graph[n - w] = 1
            
            if n + w < len(graph) and graph[n + w] != -1 and graph[n + w] != 1:
                queue.append(n + w)
                graph[n + w] = 1
        
        if len(queue) == 0:
            break

        count += 1
   
    if graph.count(0):
        return -1
        
    return count

w, h = map(int, input().split(" "))

start_lst= []
graph = []

for i in range(h):
    lst = list(map(int, input().split(" ")))
    
    for j in range(w):
        graph.append(lst[j]) 

        if lst[j] == 1:
            start_lst.append(len(graph) - 1)

visited = [False] * (w * h)

print(bfs(graph, start_lst, visited))
