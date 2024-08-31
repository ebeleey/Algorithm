N, K = map(int, input().split())

list = list(range(1, N+1))

idx = 0
step = K-1
llen = N

ans = []

while llen > 0:
    idx = (idx+step)%llen
    ans.append(list.pop(idx))
    llen -= 1

print("<", end='')
print(*ans, sep=', ', end='')
print(">")
