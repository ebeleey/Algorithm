from collections import deque
M, N = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

tomato = deque()

for i in range(N):
    for j in range(M):
        if matrix[i][j] == 1:
            tomato.append([i, j]) # 토마토 위치 큐에 넣어주깅

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

while tomato:
    i, j = tomato.popleft()
    for k in range(4):
        ni, nj = i + di[k], j + dj[k]
        if 0 <= ni < N and 0 <= nj < M and not matrix[ni][nj]:
            matrix[ni][nj] = matrix[i][j] + 1
            tomato.append([ni, nj])

def check():
    global N, M
    answer = 0
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 0:
                return -1
            if matrix[i][j] > answer:
                answer = matrix[i][j]
    return answer-1

print(check())