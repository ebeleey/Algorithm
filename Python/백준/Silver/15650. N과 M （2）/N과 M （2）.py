N, M = map(int, input().split())

def func(arr, k, m):
    if m == M:
        print(*arr)
        return
    
    for num in range(k, N+1):
        func(arr + [num], num+1, m+1)

func([], 1, 0)