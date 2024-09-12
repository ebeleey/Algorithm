N, K = map(int, input().split())

coins = list(int(input()) for _ in range(N))
cnt = 0

for i in range(N-1, -1, -1):
    while K >= coins[i]:
        K -= coins[i]
        cnt += 1

print(cnt)