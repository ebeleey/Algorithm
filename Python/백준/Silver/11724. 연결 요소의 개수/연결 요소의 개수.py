N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

cnt = 0
visited = [False] * (N+1)
for node in range(1, N+1):
    if not visited[node]:
        cnt += 1
        stack = [node]
        while stack:
            v = stack.pop()
            for i in graph[v]:
                if not visited[i]:
                    visited[i] = True
                    stack.append(i)

print(cnt)