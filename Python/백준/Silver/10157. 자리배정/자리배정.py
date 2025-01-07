C, R = map(int, input().split())
K = int(input())

seats = [[0] * C for _ in range(R)]

dc = [0, 1, 0, -1]
dr = [-1, 0, 1, 0]

if K > R*C:
    print(0)
else:
    r, c = R-1, 0
    seats[r][c] = 1

    j=0
    for i in range(2, K+1):
        while True:
            nr = r + dr[j]
            nc = c + dc[j]
            if 0<=nr<R and 0<=nc<C and not seats[nr][nc]:
                seats[nr][nc] = i
                r, c = nr, nc
                break
            else:
                j = (j+1)%4

    print(c+1, R-r)