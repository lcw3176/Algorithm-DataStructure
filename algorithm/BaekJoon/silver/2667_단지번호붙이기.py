def dfs(x, y, graph, lst, index):

    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    
    if graph[x][y] == 1:
        graph[x][y] = 0
        lst[index].append(1)
        dfs(x - 1, y, graph, lst, index)
        dfs(x, y - 1, graph, lst, index)
        dfs(x + 1, y, graph, lst, index)
        dfs(x, y + 1, graph, lst, index)
        
        return True
    return False


n = int(input())
graph = []
lst = [[]]

for i in range(n):
  graph.append(list(map(int, input())))


index = 0
for i in range(n):
    for j in range(n):
        if dfs(i, j, graph, lst, index) == True:
            index += 1
            lst.append([])
            
del lst[len(lst) - 1]
    
print(len(lst))
lst.sort(key=len)

for i in lst:
    print(len(i))