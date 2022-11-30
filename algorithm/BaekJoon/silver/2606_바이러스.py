from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        n = queue.popleft()

        for i in graph[n]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

    return visited.count(True) - 1

m = int(input())
n = int(input())

graph = [[] for i in range(m + 1)]
for i in range(n):
    lst = list(map(int, input().split(" ")))
  
    graph[lst[0]].append(lst[1])
    graph[lst[1]].append(lst[0])


visited = [False] * (m + 1)

print(bfs(graph, 1, visited))