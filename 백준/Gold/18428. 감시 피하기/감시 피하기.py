# 감시 피하기
import sys

N = int(sys.stdin.readline())
arr = [list(sys.stdin.readline().split()) for _ in range(N)] # 학생 S, 선생님 T, 아무것도 존재하지 않으면 X

# for row in arr:
#     print(row)

# 백트래킹을 쓰는 방법이 머가 있을까

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

# obstacles = []
# def set_obstacles(i, j):
#     for k in range(4):
#         stack = []
#         ni, nj = i + di[k], j + dj[k]
#         while 0 <= ni < N and 0 <= nj < N:
#             if arr[ni][nj] == 'S': # 이게 백트래킹인가??????????????????????????
#                 for item in stack:
#                     obstacles.append(item)
#                 break
#             elif arr[ni][nj] == 'X':
#                 stack.append([ni, nj])
#                 ni += di[k]
#                 nj += dj[k]
#             else:
#                 break

teachers = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 'T':
            teachers.append([i, j])

# print(obstacles)
#
# import itertools
# import copy
# combinations = list(itertools.combinations(obstacles, 3)) # 모든 조합을 고려

def can_avoid():
    for i, j in teachers:
        for k in range(4):
            ni = i +di[k]
            nj = j +dj[k]
            while 0 <= ni < N and 0 <= nj < N:
                if arr[ni][nj] == 'S':
                    return False
                elif arr[ni][nj] == 'O':
                    break
                ni += di[k]
                nj += dj[k]
    return True
# print(combinations)

# 백트래킹 함수: count는 설치된 장애물의 수
def backtrack(count):
    if count == 3:  # 장애물 3개가 설치되면 감시 여부 체크
        if can_avoid():
            return True
        return False

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'X':  # 빈 공간에 장애물 설치
                arr[i][j] = 'O'
                if backtrack(count + 1):  # 다음 장애물 설치
                    return True
                arr[i][j] = 'X'  # 백트래킹: 장애물 제거

    return False

# 백트래킹 시작
if backtrack(0):
    print("YES")
else:
    print("NO")

