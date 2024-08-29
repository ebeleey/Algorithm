# 퇴사

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

dp = [0]*(n+1) #그 날짜의 최대 수익

for i in range(n):
    T, P = arr[i]
    if i+T <= n:
        if i == 0:
            dp[i+T] = P
        else:
            dp[i+T] = max(dp[i+T], dp[i]+P, max(dp[:i])+P)

print(max(dp))