N, M = map(int, input().split())

arr = [0] + list(map(int, input().split()))
for i in range(N):
    arr[i+1] += arr[i]
for _ in range(M):
    i, j = map(int, input().split())
    print(arr[j] - arr[i-1])
