import sys
input = sys.stdin.readline

N = int(input())
nums = [0] + list(map(int, input().split()))

dp = [[0] * (N+1) for _ in range(N+1)]

# 길이 1
for i in range(1, N+1):
    dp[i][i] = 1

# 길이 2
for i in range(1, N):
    if nums[i] == nums[i+1]:
        dp[i][i+1] = 1

# 길이 3 이상
for length in range(3, N+1):
    for s in range(1, N - length + 2):
        e = s + length - 1
        if nums[s] == nums[e] and dp[s+1][e-1]:
            dp[s][e] = 1

M = int(input())

# ✅ 출력 모으기
result = []
for _ in range(M):
    S, E = map(int, input().split())
    result.append(str(dp[S][E]))

# ✅ 한 번에 출력
sys.stdout.write("\n".join(result))
