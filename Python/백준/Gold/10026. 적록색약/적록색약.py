#적록색약
from collections import deque

N = int(input())
matrix = [list(input().strip()) for _ in range(N)]

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

def bfs(x, y):
    q = deque()
    q.append([x, y])

    while q:
        i, j = q.popleft()

        for k in range(4):
            ni, nj = i+di[k], j+dj[k]

            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
                if matrix[ni][nj] == matrix[i][j]: # 같으면
                    visited[ni][nj] = 1
                    q.append([ni, nj])
    return

visited = [[0] * N for _ in range(N)]
cnt1 = 0

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j)
            cnt1 += 1

visited = [[0] * N for _ in range(N)]
cnt2 = 0


for i in range(N):
    for j in range(N):
        if matrix[i][j] == 'G':
            matrix[i][j] = 'R'


for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j)
            cnt2 += 1


print(cnt1, cnt2)






