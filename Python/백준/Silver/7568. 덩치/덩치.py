N = int(input()) #전체 사람 수
arr = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    x, y = arr[i]
    cnt = 1
    for j in range(N):
        if i != j:
            p, q = arr[j]
            if x < p and y < q:
                cnt += 1
    print(cnt, end = ' ')