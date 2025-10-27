def A(i):
    if i in memo:
        return memo[i]

    memo[i] = A(i//P) + A(i//Q)    
    return memo[i]

N, P, Q = map(int, input().split())
memo = {0: 1}
print(A(N))