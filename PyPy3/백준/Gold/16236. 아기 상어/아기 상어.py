from collections import deque

N = int(input())  # 공간의 크기
arr = [list(map(int, input().split())) for _ in range(N)]  # 공간의 상태

fish_pos = []  # 물고기들의 위치(필수는 아니지만 네 구조 유지)
time = 0       # ★ ans 대신 time 사용 (아래 print도 time)

# 상어 초기 위치 세팅
for x in range(N):
    for y in range(N):
        if arr[x][y] == 9:
            shark_pos = (x, y)
            arr[x][y] = 0  # 상어 표식은 빈 칸으로 전환

shark_size = 2
eat_cnt = 0

# 방향: ↑, ←, →, ↓
di = [-1, 0, 0, 1]
dj = [0, -1, 1, 0]

# 아기 상어 위치에서 한 번의 BFS로 "가장 가까운 먹잇감" 찾기
def calculate_distance(si, sj, size):
    q = deque([(si, sj, 0)])  # (i, j, dist) 형태로만 운영
    visited = [[False] * N for _ in range(N)]
    visited[si][sj] = True

    fish = []            # (dist, i, j)
    min_dist = -1        # 첫 후보 거리 기록용

    while q:
        i, j, dist = q.popleft()

        # 이미 후보가 있고, 더 먼 레벨로 넘어가면 중단
        if dist > min_dist >= 0:
            break

        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
                # 이동 가능(통과 가능): 칸의 값 <= 상어 크기
                if arr[ni][nj] <= size:
                    visited[ni][nj] = True
                    next_dist = dist + 1

                    # 먹을 수 있으면 후보 등록
                    if 0 < arr[ni][nj] < size:
                        fish.append((next_dist, ni, nj))
                        if min_dist == -1:
                            min_dist = next_dist

                    # ★ 큐에는 (ni, nj, next_dist)만 넣는다 (중복 push 제거)
                    q.append((ni, nj, next_dist))

    if not fish:
        return None

    fish.sort()  # 거리 → 행 → 열
    return fish[0]  # (dist, i, j)

def decide_direction():
    si, sj = shark_pos
    next_fish = calculate_distance(si, sj, shark_size)
    return next_fish  # (dist, i, j) 또는 None

# 시뮬레이션 루프
while True:
    next_fish = decide_direction()

    if next_fish is None:
        break

    dist, fi, fj = next_fish

    time += dist
    shark_pos = (fi, fj)
    arr[fi][fj] = 0
    eat_cnt += 1

    if eat_cnt == shark_size:
        shark_size += 1
        eat_cnt = 0

print(time)
