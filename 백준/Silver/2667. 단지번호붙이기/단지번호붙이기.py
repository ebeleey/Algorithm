# 단지 번호 붙이기
from collections import deque

N = int(input()) # 지도의 크기

matrix = [list(map(int, input().strip())) for _ in range(N)]

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

count_list = []
visited = [[0] * N for _ in range(N)]

for r in range(N):
    for c in range(N):
        if matrix[r][c] and not visited[r][c]:
            visited[r][c] = 1 # 방문 처리
            q = deque()
            q.append([r, c])
            cnt = 1
            while q:
                i, j = q.popleft()
                for k in range(4):
                    ni = i + di[k]
                    nj = j + dj[k]
                    if 0 <= ni < N and 0 <= nj < N and matrix[ni][nj] and not visited[ni][nj]:
                        q.append([ni, nj])
                        visited[ni][nj] = 1
                        cnt += 1
            count_list.append(cnt)
count_list.sort()
print(len(count_list))
print(*count_list, sep='\n')

