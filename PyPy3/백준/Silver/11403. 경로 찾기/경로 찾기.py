from collections import deque

def bfs(start):
    visited = [0] * N
    queue = deque([start])

    while queue:
        node = queue.popleft()

        for next in graph[node]:
            if not visited[next]:
                queue.append(next)
                visited[next] = 1

    return visited

N = int(input()) # 정점의 개수

graph = [[] for _ in range(N)]

for i in range(N):
    nodes = list(map(int, input().split()))
    
    for j in range(N):
        if nodes[j]:
            graph[i].append(j)

for i in range(N):
    result = bfs(i)
    print(*result)