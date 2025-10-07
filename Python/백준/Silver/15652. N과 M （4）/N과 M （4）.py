N, M = map(int, input().split())

def func(arr, k):
    # 종료 조건
    if len(arr) == M:
        print(*arr)
        return
    
    for num in range(k, N+1):
        func(arr + [num], num)

func([], 1)