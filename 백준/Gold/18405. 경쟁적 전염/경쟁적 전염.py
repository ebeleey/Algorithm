# 경쟁적 전염

import sys

N, K = map(int, sys.stdin.readline().split())  # 시험관 크기 N, 바이러스 번호 최댓값 K
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]  # 시험관 정보
S, X, Y = map(int, sys.stdin.readline().split())  # S초 뒤에 (X,Y)에 존재하는 바이러스의 종류 출력하기
# 존재하지 않으면 0 출력

virus = []

for i in range(N):
    for j in range(N):  # 바이러스 위치 저장하기
        if arr[i][j]:  # 0이 아니면 (바이러스라면)
            virus.append([arr[i][j], 0, i, j]) # [바이러스 번호, 시간, 행, 열]

from collections import deque

virus.sort() # 바이러스 번호가 낮은 순서대로 정렬
queue = deque(virus)

di = [1, -1, 0, 0]  # 바이러스는 상하좌우로 증식
dj = [0, 0, 1, -1]

while queue:
    num, sec, i, j = queue.popleft()
    if sec == S:
        break
    for k in range(4):
        ni, nj = i +di[k], j + dj[k]
        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 0:
            arr[ni][nj] = num
            queue.append([num, sec+1, ni, nj])

print(arr[X-1][Y-1])