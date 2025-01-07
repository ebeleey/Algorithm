# DFS를 사용하여 미로에서 출발점에서 도착점까지 갈 수 있는지 확인하는 함수
def dfs(maze, x, y):
    # 현재 위치가 미로 범위를 벗어나거나 벽(1)을 만나면 False를 반환
    if x < 0 or x >= 16 or y < 0 or y >= 16 or maze[x][y] == 1:
        return False

    # 현재 위치가 도착점(3)이라면 True 반환
    if maze[x][y] == 3:
        return True

    # 현재 위치를 방문했음을 표시하기 위해 벽(1)으로 변경
    maze[x][y] = 1

    # 상, 하, 좌, 우로 이동하면서 도착점까지 갈 수 있는지 탐색
    if dfs(maze, x - 1, y) or dfs(maze, x + 1, y) or dfs(maze, x, y - 1) or dfs(maze, x, y + 1):
        return True

    return False


# 10개의 테스트 케이스를 처리하는 메인 함수
for _ in range(10):
    # 테스트 케이스 번호 입력 (여기선 생략해도 됨)
    tc = int(input())
    # 16x16 미로 입력
    maze = [list(map(int, input().strip())) for _ in range(16)]

    # 출발점은 (1, 1)에서 시작하므로 dfs를 호출하여 경로를 찾음
    if dfs(maze, 1, 1):
        print(f"#{tc} 1")  # 도달 가능하면 1 출력
    else:
        print(f"#{tc} 0")  # 도달 불가능하면 0 출력
