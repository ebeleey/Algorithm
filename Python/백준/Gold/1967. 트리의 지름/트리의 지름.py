import sys
sys.setrecursionlimit(10**6)

n = int(input()) # 노드의 개수

graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    p, c, w = map(int, input().split())
    graph[p].append((c, w))
    graph[c].append((p, w))

visited = [False] * (n+1)

max_dist = 0
max_node = 0

def dfs(node, dist):
    global max_dist, max_node

    visited[node] = True

    if dist > max_dist:
        max_dist = dist
        max_node = node


    for next, weight in graph[node]:
        if not visited[next]:
            dfs(next, dist + weight)

dfs(1, 0)

visited = [False] * (n+1)
max_dist = 0

dfs(max_node, 0)

print(max_dist)