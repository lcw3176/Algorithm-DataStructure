import sys
sys.setrecursionlimit(10**5)

def dfs(x, y, graph, w, h):

    if x <= -1 or x >= h or y <= -1 or y >= w:
        return False
    
    if graph[x][y] == 1:
        graph[x][y] = 0

        dfs(x - 1, y, graph, w, h)
        dfs(x, y - 1, graph, w, h)
        dfs(x + 1, y, graph, w, h)
        dfs(x, y + 1, graph, w, h)
        
        return True
    return False


n = int(input())

for _ in range(n):
    w, h, k = map(int, input().split(" "))
    graph = [[0 for _ in range(w)] for _ in range(h)]

    
    for i in range(k):
        y, x  = map(int, input().split(" "))
        graph[x][y] = 1

    index = 0
    for i in range(h):
        for j in range(w):
            if dfs(i, j, graph, w, h):
                index += 1

    print(index)
    