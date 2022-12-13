from collections import deque


def bfs(start, target, visited):
    queue = deque([start])
    count = -1
    flag = True

    while flag:
        lst = []
        while queue:
            lst.append(queue.popleft())

        for n in lst:
            if n == target:
                flag = False
                break

            if n - 1 >= 0 and not visited[n - 1]:
                queue.append(n - 1)
                visited[n - 1] = True
            
            if  n + 1 < len(visited) and not visited[n + 1]:
                queue.append(n + 1)
                visited[n + 1] = True
            
            if  n * 2 < len(visited) and not visited[n * 2]:
                queue.append(n * 2)
                visited[n * 2] = True
        
        count += 1
   
    return count

start, target = map(int, input().split(" "))
print(bfs(start, target, [False for i in range(110000)]))
