N, M = map(int, input().split())
board = [list(input().strip()) for _ in range(N)]

sr, sc = 0, 0
cnts = []

for sr in range(0, N-7):
    for sc in range(0, M-7):
        cnt = 0
        for i in range(sr, sr + 8, 2):
            # 맨 왼쪽 위가 W인 경우
            for j in range(sc, sc + 8, 2):
                if board[i][j] != 'W':
                    cnt += 1
                if board[i][j + 1] != 'B':
                    cnt += 1
                if board[i + 1][j] != 'B':
                    cnt += 1
                if board[i + 1][j + 1] != 'W':
                    cnt += 1
        cnts.append(cnt)
        cnts.append(64 - cnt)  #맨 왼쪽 위가 B인 경우


print(min(cnts))