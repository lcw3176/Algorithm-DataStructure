from collections import deque

n, m = map(int, input().split(" "))

graph = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]
maps = [0 for _ in range(n + 1)]

for _ in range(1, m + 1):
    i, j = map(int, input().split(" "))
    graph[i].append(j)
    graph[j].append(i)


def bfs(graph, visited, start):
    queue = deque([start])
    copy_visited = [i for i in visited]
    visited[start] = True

    while queue:
        n = queue.popleft()

        for i in graph[n]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

    if visited == copy_visited:
        return 0
    
    return 1

count = 0

for i in range(1, n + 1):
    count += bfs(graph, visited, i)

print(count)