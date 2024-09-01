N, K = map(int, input().split()) # 물품의 수 N, 준서가 버틸 수 있는 무게 K

dp = [0]*(K+1)

items = [list(map(int, input().split())) for _ in range(N)]

# print(items)

for w, v in items:
    for i in range(K, -1, -1):
        if i + w <= K:
            if dp[i+w] < dp[i]+v:
                dp[i+w] = dp[i]+v
print(dp[K])