from collections import deque

N, M = map(int, input().split())

campus = [list(input()) for _ in range(N)]
visited= [[False] * M for _ in range(N)]

doyeon = deque([])

for i in range(N):
    for j in range(M):
        if campus[i][j] == 'I':
            doyeon.append((i, j))
            visited[i][j] = True

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

count = 0

while doyeon:
    i, j = doyeon.popleft()
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]

        if not 0 <= ni < N or not 0 <= nj < M or visited[ni][nj]:
            continue

        if campus[ni][nj] != 'X':
            if campus[ni][nj] == 'P':
                count += 1  
            doyeon.append((ni, nj))
            visited[ni][nj] = True

if count:
    print(count)
else:
    print('TT')