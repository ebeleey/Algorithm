import sys

N, M = map(int, sys.stdin.readline().split()) # 세로 N 가로 M
area = [list(map(int, sys.stdin.readline().split())) for _ in range(N) ]

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]
max_safety = 0


# 바이러스 증식
def replicateVirus(virus, area):
    for item in virus:
        i = item[0]
        j = item[1]
        for k in range(4): # 상하좌우   
            ni, nj = i + di[k], j + dj[k] 
            if 0 <= ni < N and 0 <= nj < M and area[ni][nj] == 0: # 연구소 안에서, 벽이 아닌 곳이면
                area[ni][nj] = 2 # 바이러스 증식 !
                replicateVirus([[ni, nj]], area)
    return area

empty = []
wall = []
virus = []

for i in range(N):
    for j in range(M): 
        if area[i][j] == 0:         # 빈 칸 (0) 
            empty.append([i, j])
        elif area[i][j] == 1:       # 벽 (1)
            wall.append([i, j])
        else:                       # 바이러스 (2)
            virus.append([i, j])

import itertools
combinations = list(itertools.combinations(empty, 3))

import copy

for item in combinations:
    copy_area = copy.deepcopy(area)

    copy_area[item[0][0]][item[0][1]] = 3
    copy_area[item[1][0]][item[1][1]] = 3
    copy_area[item[2][0]][item[2][1]] = 3
    
    # for row in copy_area:
    #     print(row)
    # print()
    result = []
    result = replicateVirus(virus, copy_area)

    safety = 0
    for row in result:
        # print(row)
        safety += row.count(0)
    if safety > max_safety:
        max_safety = safety
    
print(max_safety)