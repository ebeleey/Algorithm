from collections import deque

R, C = map(int, input().split())
cave = [list(input()) for _ in range(R)]

N = int(input())
heights = list(map(int, input().split()))

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def throw(row, is_left):
    if is_left:
        for col in range(C):
            if cave[row][col] == 'x':
                cave[row][col] = '.'
                return row, col
    else:
        for col in range(C - 1, -1, -1):
            if cave[row][col] == 'x':
                cave[row][col] = '.'
                return row, col
    return -1, -1

def find_floating_cluster():
    visited = [[False] * C for _ in range(R)]

    # 바닥에 닿은 클러스터 탐색
    for col in range(C):
        if cave[R-1][col] == 'x' and not visited[R-1][col]:
            q = deque()
            q.append((R-1, col))
            visited[R-1][col] = True
            while q:
                r, c = q.popleft()
                for k in range(4):
                    nr, nc = r + dr[k], c + dc[k]
                    if 0 <= nr < R and 0 <= nc < C:
                        if cave[nr][nc] == 'x' and not visited[nr][nc]:
                            visited[nr][nc] = True
                            q.append((nr, nc))

    cluster = []
    for r in range(R):
        for c in range(C):
            if cave[r][c] == 'x' and not visited[r][c]:
                cluster.append((r, c))
    return cluster

def fall(cluster):
    # 먼저 제거
    for r, c in cluster:
        cave[r][c] = '.'

    # 얼마나 떨어질 수 있는지 계산
    min_fall = R
    cluster_set = set(cluster)
    for r, c in cluster:
        nr = r + 1
        dist = 0
        while nr < R and (cave[nr][c] == '.' or (nr, c) in cluster_set):
            nr += 1
            dist += 1
        min_fall = min(min_fall, dist)

    # 떨어진 위치에 다시 배치
    for r, c in sorted(cluster, reverse=True):
        cave[r + min_fall][c] = 'x'

# 메인 로직
for i in range(N):
    height = heights[i]
    is_left = (i % 2 == 0)

    r, c = throw(R - height, is_left)
    if r == -1:
        continue

    cluster = find_floating_cluster()
    if cluster:
        fall(cluster)

for row in cave:
    print(''.join(row))