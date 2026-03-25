from collections import deque

N = int(input()) # 노드의 개수

graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

parent = [0] * (N+1)
visited = [False] * (N+1)

# def dfs(node):
#     visited[node] = True

#     for next in graph[node]:
#         if not visited[next]:
#             parent[next] = node
#             dfs(next)

# dfs(1)
q = deque([])

def bfs(start) : 
    q.append(start)

    visited[start] = True

    while q:
        node = q.popleft()

        for next in graph[node]:
            if not visited[next]:
                q.append(next)
                visited[next] = True
                parent[next] = node

bfs(1)

for i in range(2, N+1):
    print(parent[i])