INF = int(1e9)

N, M = map(int, input().split()) # 유저의 수 N, 친구 관계의 수 M

# 2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화
graph = [[INF] * (N+1) for _ in range(N+1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for i in range(1, N+1):
    graph[i][i] = 0

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

min_bacon = INF
answer = 0

for i in range(1, N+1):
    bacon = sum(graph[i][1:N+1])
    if bacon < min_bacon:
        min_bacon = bacon
        answer = i

print(answer)