import heapq

INF =  int(1e9)
N, E = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(E):
    # a번 정점에서 b번 정점까까지 양방향 길이 존재하며, 그 거리가 c라는 뜻
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split()) # 반드시 거쳐야 하는 두 개의 다른 정점 번호


# 1번 정점에서 N번 정점으로 최단 거리로 이동
# 주어진 두 정점을 반드시 거치면서 최단 경로로 이동

def dijkstra(start, end):
    q = []
    heapq.heappush(q, (0, start))
    
    distance = [INF] * (N+1)
    distance[start] = 0
    

    while q: # 큐가 비어있지 않다면
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue
            
        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    return distance[end]

result = min(dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, N),
      dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, N))

print(result if result < INF else -1)

