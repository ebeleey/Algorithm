N = int(input()) # 수열 A의 길이
A = list(map(int, input().split()))
M = int(input()) # 수열 B의 길이
B = list(map(int, input().split()))

i, j = 0, 0
ans = []

while True:
    commons = set(A[i:]) & set(B[j:])

    if not commons:
        break

    max_val = max(commons)

    ni = i
    while ni < N:
        if A[ni] == max_val:
            break
        ni += 1
    
    nj = j
    while nj < M:
        if B[nj] == max_val:
            break
        nj += 1
        
    ans.append(max_val)
    i = ni + 1
    j = nj + 1

print(len(ans))
if ans:
    print(*ans)