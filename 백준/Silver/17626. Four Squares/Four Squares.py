n = int(input())

dp = [10e10000] * (n+1)

dp[0] = 0

for num in range(1, n+1):
    if num**(1/2) % 1 == 0: #제곱수면
        dp[num] = 1
    else:
        for i in range(1, int(num**(1/2))+1):
            dp[num] = min(dp[num], dp[num-i*i]+dp[i*i])

print(dp[n])
