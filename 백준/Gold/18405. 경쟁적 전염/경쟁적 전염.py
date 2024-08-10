# 경쟁적 전염

import sys

N, K = map(int, sys.stdin.readline().split()) # 시험관 크기 N, 바이러스 번호 최댓값 K
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)] # 시험관 정보
S, X, Y = map(int, sys.stdin.readline().split()) # S초 뒤에 (X,Y)에 존재하는 바이러스의 종류 출력하기 
                                                 # 존재하지 않으면 0 출력


di = [1, -1, 0, 0] # 바이러스는 상하좌우로 증식
dj = [0, 0, 1, -1]

def replicateVirus(idx, i, j): # 바이러스 번호, 위치
    visited[i][j] = True
    for l in range(4):
        ni, nj = i + di[l], j + dj[l]
        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 0 and not visited[ni][nj]:
            visited[ni][nj] = True
            arr[ni][nj] = idx
            temp.append([ni, nj])


virus = [[] for _ in range(K+1)]

for i in range(N):
    for j in range(N):  # 바이러스 위치 저장하기
        if arr[i][j]:   # 0이 아니면 (바이러스라면)
            virus[arr[i][j]].append([i, j])
    
for sec in range(1, S+1):
    if arr[X-1][Y-1]:
        break

    visited = [[False] * N for _ in range(N)] # 하루에 한 번씩 visited 배열 초기화
    for idx in range(1, K+1):
        temp = []
        if virus[idx]: # 바이러스가 있으면
            for pos in virus[idx]:
                replicateVirus(idx, *pos)
            for item in temp:
                virus[idx].append(item)

print(arr[X-1][Y-1])
