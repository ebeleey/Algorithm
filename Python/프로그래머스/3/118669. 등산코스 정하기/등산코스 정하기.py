from heapq import heappush, heappop

INF = int(1e9)

def solution(n, paths, gates, summits): # gates 출입구, summits 산봉우리
    distance = [INF] * (n+1)

    graph = [[] for _ in range(n+1)]
    for u, v, w in paths:
        graph[u].append((v, w))
        graph[v].append((u, w))

    summits.sort()
    
    gates_set = set(gates)
    summits_set = set(summits)
    
    for gate in gates:  # 츌발점
        q = []
        heappush(q, (0, gate))
        distance[gate] = 0

        while q: # 큐가 빌 때 까지
            dist, now = heappop(q) # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기

            if dist > distance[now] or now in summits_set: # 봉우리이거나 현재 노드가 이미 처리된 적 있는 노드라면 무시
                break

            for node, new_dist in graph[now]:  # 현재 노드와 연결된 다른 인접한 노드들을 확인
                tmp = max(dist, new_dist) 
                if tmp< distance[node] and node not in gates_set: #다른 출입구 방문하면 안 됨
                    distance[node] = tmp
                    heappush(q, (tmp, node))
                    
    min_intensity = INF
    summit_num = 0                
    
    for summit in summits: # 도착점
        if distance[summit] < min_intensity:
            min_intensity = distance[summit]
            summit_num = summit

    return [summit_num, min_intensity] # [산봉우리의 번호, intensity의 최솟값]
